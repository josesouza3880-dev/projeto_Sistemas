import os
import re
import shutil
import time
import csv
import logging
import logging.handlers
import threading
import tempfile
import unicodedata
from datetime import datetime
from pathlib import Path
from pypdf import PdfReader

# ============================================================
#  SISTEMA MN-AutoPorto v4.0 — Diário de Bordo Automático
#  Autor: josluiz
#  v4.0 — Revisão MASTER: 8 vulnerabilidades críticas corrigidas
# ============================================================

P_SCAN      = Path('/home/josluiz/SCAN')
P_DEST_BASE = Path('/home/josluiz/DEST')
LOG_CSV     = Path('/home/josluiz/relatorio_movimentacao.csv')
LOG_AUDIT   = Path('/home/josluiz/auditoria.log')

TAMANHO_MAXIMO_MB  = 50
INTERVALO_SEGUNDOS = 5
ESPACO_MINIMO_MB   = 100   # MASTER #5: aborta se disco tiver menos que isso livre

CABECALHO_CSV = [
    'Nome Original', 'Nome Final', 'Data do Documento',
    'Turno', 'Pasta Destino', 'Tamanho (KB)', 'Data Processamento', 'Status'
]

MESES_EXTENSO = {
    'janeiro': 1, 'fevereiro': 2, 'março': 3, 'marco': 3,
    'abril': 4, 'maio': 5, 'junho': 6, 'julho': 7,
    'agosto': 8, 'setembro': 9, 'outubro': 10,
    'novembro': 11, 'dezembro': 12
}

# MASTER #8: lock global — garante que só uma thread escreve no CSV por vez
_csv_lock = threading.Lock()

# MASTER #8: conjunto de arquivos em processamento — evita processar o mesmo
# arquivo duas vezes se o ciclo demorar mais que INTERVALO_SEGUNDOS
_em_processamento: set = set()
_processamento_lock = threading.Lock()


# ── Configuração ─────────────────────────────────────────────

def configurar_log():
    """
    MASTER #6: logging.basicConfig não rotaciona o arquivo — em produção
    o auditoria.log crescia indefinidamente até encher o disco.
    Solução: RotatingFileHandler com limite de 5 MB e 3 backups.
    """
    handler = logging.handlers.RotatingFileHandler(
        LOG_AUDIT,
        maxBytes=5 * 1024 * 1024,   # 5 MB por arquivo
        backupCount=3,               # mantém auditoria.log.1, .2, .3
        encoding='utf-8'
    )
    handler.setFormatter(logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    ))
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)


def garantir_estrutura():
    P_SCAN.mkdir(parents=True, exist_ok=True)
    P_DEST_BASE.mkdir(parents=True, exist_ok=True)
    (P_DEST_BASE / 'QUARENTENA').mkdir(exist_ok=True)
    (P_DEST_BASE / 'SEM_DATA').mkdir(exist_ok=True)

    if not LOG_CSV.exists():
        with open(LOG_CSV, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f, delimiter=';').writerow(CABECALHO_CSV)
        print(f"  [LOG] Relatório criado: {LOG_CSV}")


# ── Segurança: validação de caminho ──────────────────────────

def caminho_seguro(pasta_base: Path, nome_arquivo: str) -> Path:
    """
    MASTER #1 — PATH INJECTION / DIRECTORY TRAVERSAL:
    Um arquivo chamado '../../etc/passwd.pdf' ou '../DEST/outro.pdf'
    faria o shutil.move() escrever FORA das pastas autorizadas.
    Em porto isso é crítico — poderia sobrescrever arquivos do sistema.

    Solução: extrair só o nome base (sem barras) e confirmar que o
    caminho resolvido está dentro da pasta autorizada.
    """
    nome_limpo = Path(nome_arquivo).name          # remove qualquer '../'
    destino    = (pasta_base / nome_limpo).resolve()
    base_real  = pasta_base.resolve()

    if not str(destino).startswith(str(base_real)):
        raise PermissionError(
            f"BLOQUEADO: tentativa de path injection → '{nome_arquivo}'"
        )
    return destino


def sanitizar_nome(nome: str) -> str:
    """
    MASTER #1b — normaliza acentos e remove caracteres perigosos do nome
    do arquivo antes de usar no sistema de arquivos.
    Ex: 'diário: bordo/março.pdf' → 'diario bordo marco.pdf'
    """
    # Normaliza unicode → ASCII (remove acentos)
    nome_ascii = unicodedata.normalize('NFKD', nome)
    nome_ascii = nome_ascii.encode('ascii', 'ignore').decode('ascii')
    # Remove caracteres perigosos para nomes de arquivo
    nome_limpo = re.sub(r'[\\/:*?"<>|]', '_', nome_ascii)
    return nome_limpo.strip()


# ── Verificação de disco ──────────────────────────────────────

def verificar_espaco_disco() -> bool:
    """
    MASTER #5 — DISCO CHEIO:
    shutil.move() falha com OSError sem mensagem clara se o disco
    estiver cheio. O arquivo some do SCAN mas não chega ao DEST —
    perda irreversível de documento.

    Solução: verificar espaço livre ANTES de qualquer operação de escrita.
    """
    stat = shutil.disk_usage(P_DEST_BASE)
    livre_mb = stat.free / (1024 * 1024)
    if livre_mb < ESPACO_MINIMO_MB:
        logging.critical(f"DISCO QUASE CHEIO: {livre_mb:.1f} MB livres. Operação suspensa.")
        print(f"\n  ✖ ALERTA: disco com apenas {livre_mb:.1f} MB livres!")
        print(f"  ✖ Sistema suspenso até liberar espaço (mínimo: {ESPACO_MINIMO_MB} MB)\n")
        return False
    return True


# ── Leitura do PDF ───────────────────────────────────────────

def extrair_texto_pdf(caminho: Path) -> str:
    """
    MASTER #2 — PDF MALFORMADO / BOMBA:
    PDFs corrompidos ou mal-formados podem travar o PdfReader
    em loop infinito consumindo 100% de CPU.
    Solução: timeout via threading — se demorar mais de 10s, abandona.

    MASTER #3 — ENCODING DO TEXTO EXTRAÍDO:
    pypdf pode retornar texto com caracteres de controle invisíveis
    (ex: \x00, \x01) que quebram os regex de data e turno.
    Solução: limpar o texto antes de retornar.
    """
    resultado = ['']
    erro      = [None]

    def _ler():
        try:
            reader = PdfReader(str(caminho))
            texto  = ''
            for page in reader.pages:
                texto += page.extract_text() or ''
            # MASTER #3: remove caracteres de controle exceto \n e \t
            texto = re.sub(r'[\x00-\x08\x0b-\x1f\x7f]', ' ', texto)
            resultado[0] = texto
        except Exception as e:
            erro[0] = e

    for tentativa in range(3):
        t = threading.Thread(target=_ler, daemon=True)
        t.start()
        t.join(timeout=10)      # MASTER #2: 10 segundos máximo

        if t.is_alive():
            logging.error(f"PDF travou leitura (possível bomba/corrompido): {caminho.name}")
            return ''           # abandona — não mata o robô

        if erro[0] is None:
            return resultado[0]

        if tentativa < 2:
            time.sleep(1)

    logging.warning(f"Falha ao ler PDF após 3 tentativas: {caminho.name} | {erro[0]}")
    return ''


# ── Detecção de data ─────────────────────────────────────────

def detectar_data(texto: str) -> datetime | None:
    """
    MASTER #4 — CATASTROPHIC BACKTRACKING:
    O padrão original r'\b(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})\b'
    com \w+ em texto longo e mal-formatado pode causar backtracking
    exponencial — o regex trava o processo por segundos ou minutos.

    Solução: substituir \w+ por \w{3,12} (limite explícito de tamanho)
    para eliminar o backtracking catastrófico.
    """
    if not texto:
        return None

    # Padrão numérico: DD/MM/AAAA
    padrao_numerico = r'\b(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{4})\b'
    for match in re.finditer(padrao_numerico, texto):
        try:
            dia, mes, ano = int(match.group(1)), int(match.group(2)), int(match.group(3))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
                return datetime(ano, mes, dia)
        except ValueError:
            continue

    # MASTER #4: \w{3,12} no lugar de \w+
    padrao_extenso = r'\b(\d{1,2})\s+de\s+(\w{3,12})\s+de\s+(\d{4})\b'
    match = re.search(padrao_extenso, texto, re.IGNORECASE)
    if match:
        try:
            dia      = int(match.group(1))
            mes_nome = match.group(2).lower()
            ano      = int(match.group(3))
            mes      = MESES_EXTENSO.get(mes_nome)
            if mes:
                return datetime(ano, mes, dia)
        except ValueError:
            pass

    padrao_mes_ano = r'\b(' + '|'.join(MESES_EXTENSO.keys()) + r')\s+de\s+(\d{4})\b'
    match = re.search(padrao_mes_ano, texto, re.IGNORECASE)
    if match:
        try:
            mes = MESES_EXTENSO.get(match.group(1).lower())
            ano = int(match.group(2))
            if mes:
                return datetime(ano, mes, 1)
        except ValueError:
            pass

    return None


# ── Detecção de turno ────────────────────────────────────────

def detectar_turno(texto: str) -> str:
    if not texto:
        return 'SemTurno'

    match = re.search(r'(\d)[°º]\s*turno\b', texto, re.IGNORECASE)
    if match:
        return f"Turno{match.group(1)}"

    match = re.search(r'\bturno\s*[:\-]?\s*(\d)\b', texto, re.IGNORECASE)
    if match:
        return f"Turno{match.group(1)}"

    extensos = {
        'primeiro': '1', 'segundo': '2', 'terceiro': '3',
        'quarto': '4', 'quinto': '5'
    }
    for palavra, num in extensos.items():
        if re.search(rf'\b{palavra}\s+turno\b', texto, re.IGNORECASE):
            return f"Turno{num}"

    return 'SemTurno'


# ── Organização e movimentação ───────────────────────────────

def pasta_do_mes(data_doc: datetime) -> tuple[Path, str]:
    nome_pasta = f"{data_doc.month:02d}-{data_doc.year}"
    caminho    = P_DEST_BASE / nome_pasta
    caminho.mkdir(exist_ok=True)
    return caminho, nome_pasta


def nome_unico(pasta: Path, novo_nome: str) -> str:
    base, ext = os.path.splitext(novo_nome)
    if not ext:
        ext = '.pdf'
    candidato = novo_nome
    contador  = 2
    while (pasta / candidato).exists():
        candidato = f"{base}_{contador}{ext}"
        contador += 1
    return candidato


def registrar_csv(nome_orig, nome_final, data_doc, turno,
                  pasta_dest, tamanho_kb, agora, status):
    """
    MASTER #8: lock garante que duas threads nunca escrevem
    ao mesmo tempo — sem lock, duas linhas simultâneas corrompem o CSV.
    """
    with _csv_lock:
        for tentativa in range(3):
            try:
                with open(LOG_CSV, 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f, delimiter=';').writerow([
                        nome_orig, nome_final, data_doc, turno,
                        pasta_dest, tamanho_kb, agora, status
                    ])
                return
            except PermissionError:
                if tentativa < 2:
                    time.sleep(0.5)
                else:
                    logging.warning(
                        f"CSV bloqueado após 3 tentativas. "
                        f"Registro perdido: {nome_orig} | {status}"
                    )
                    print("  ⚠ Aviso: feche o Excel/LibreOffice durante a operação.")


# ── Processamento principal ──────────────────────────────────

def processar_arquivo(nome: str):
    """
    MASTER #7 — ATOMICIDADE DA MOVIMENTAÇÃO:
    shutil.move() entre partições diferentes faz CÓPIA + DELETE.
    Se a luz cair no meio, o arquivo fica duplicado (origem e destino)
    ou corrompido. O robô não tem como saber o que aconteceu.

    Solução: copiar para arquivo TEMPORÁRIO no destino primeiro,
    verificar integridade (tamanho), depois deletar a origem.
    Assim nunca há perda de documento.
    """
    # MASTER #8: evita processar o mesmo arquivo em paralelo
    with _processamento_lock:
        if nome in _em_processamento:
            return
        _em_processamento.add(nome)

    try:
        agora_dt   = datetime.now()
        agora_str  = agora_dt.strftime('%d/%m/%Y %H:%M:%S')
        origem     = P_SCAN / nome
        tamanho_kb = round(origem.stat().st_size / 1024, 2)
        tamanho_mb = tamanho_kb / 1024
        ext        = origem.suffix.lower()

        # Verifica espaço em disco antes de tudo
        if not verificar_espaco_disco():
            return

        # MASTER #1: sanitiza o nome antes de qualquer operação
        nome_sanitizado = sanitizar_nome(nome)

        # Quarentena para arquivos grandes
        if tamanho_mb > TAMANHO_MAXIMO_MB:
            pasta_dest = P_DEST_BASE / 'QUARENTENA'
            novo_nome  = nome_unico(pasta_dest, f"QUARENTENA_{nome_sanitizado}")
            _mover_atomico(origem, pasta_dest / novo_nome)
            registrar_csv(nome, novo_nome, '-', '-', 'QUARENTENA',
                          tamanho_kb, agora_str, 'QUARENTENA')
            print(f"  ⚠ [QUARENTENA] {nome} ({tamanho_kb} KB)")
            logging.warning(f"QUARENTENA | {nome} | {tamanho_kb} KB")
            return

        # Lê e extrai informações do PDF
        data_doc = None
        turno    = 'SemTurno'

        if ext == '.pdf':
            texto    = extrair_texto_pdf(origem)
            data_doc = detectar_data(texto)
            turno    = detectar_turno(texto)

        # Define destino
        if data_doc:
            pasta_dest, nome_pasta = pasta_do_mes(data_doc)
            data_str  = data_doc.strftime('%d-%m-%Y')
            novo_nome = nome_unico(pasta_dest, f"DiarioDeBordo_{data_str}_{turno}.pdf")
            status    = 'MOVIDO'
        else:
            pasta_dest = P_DEST_BASE / 'SEM_DATA'
            nome_pasta = 'SEM_DATA'
            novo_nome  = nome_unico(pasta_dest, f"DiarioDeBordo_SemData_{turno}_{nome_sanitizado}")
            status     = 'SEM_DATA'

        destino_full = pasta_dest / novo_nome

        # MASTER #1: valida que o destino está dentro da pasta autorizada
        caminho_seguro(pasta_dest, novo_nome)

        _mover_atomico(origem, destino_full)

        data_exib = data_doc.strftime('%d/%m/%Y') if data_doc else '-'
        registrar_csv(nome, novo_nome, data_exib, turno,
                      nome_pasta, tamanho_kb, agora_str, status)
        logging.info(f"{status} | {nome} → {nome_pasta}/{novo_nome}")

        icone = '✔' if status == 'MOVIDO' else '⚠'
        print(f"  {icone} {nome}")
        print(f"      Data detectada : {data_exib}")
        print(f"      Turno detectado: {turno}")
        print(f"      Salvo em       : {nome_pasta}/{novo_nome}")

    except Exception as e:
        registrar_csv(nome, '-', '-', '-', '-', 0, datetime.now().strftime('%d/%m/%Y %H:%M:%S'), f'ERRO: {e}')
        logging.error(f"ERRO | {nome} | {e}")
        print(f"  ✖ ERRO em {nome}: {e}")

    finally:
        # MASTER #8: sempre remove do conjunto, mesmo se der erro
        with _processamento_lock:
            _em_processamento.discard(nome)


def _mover_atomico(origem: Path, destino: Path):
    """
    MASTER #7 — Move arquivo com segurança:
    1. Copia para arquivo temporário DENTRO da pasta de destino
    2. Verifica que o tamanho bate com o original
    3. Só então deleta a origem
    Se qualquer passo falhar, a origem é preservada.
    """
    pasta_destino = destino.parent
    tamanho_orig  = origem.stat().st_size

    # Arquivo temporário na mesma partição do destino (evita cópia entre partições no rename)
    tmp_fd, tmp_path = tempfile.mkstemp(dir=pasta_destino, suffix='.tmp')
    os.close(tmp_fd)
    tmp_path = Path(tmp_path)

    try:
        shutil.copy2(str(origem), str(tmp_path))

        # Verifica integridade pelo tamanho
        if tmp_path.stat().st_size != tamanho_orig:
            raise IOError(
                f"Tamanho divergente após cópia: "
                f"orig={tamanho_orig}B, cópia={tmp_path.stat().st_size}B"
            )

        tmp_path.rename(destino)    # rename atômico no mesmo filesystem
        origem.unlink()             # só deleta a origem depois de confirmado

    except Exception:
        # Limpeza: remove o temporário se algo deu errado
        if tmp_path.exists():
            tmp_path.unlink()
        raise


# ── Loop principal ───────────────────────────────────────────

def ciclo_varredura():
    try:
        arquivos = [
            a for a in os.listdir(P_SCAN)
            if (P_SCAN / a).is_file()
        ]
    except OSError as e:
        logging.error(f"Falha ao listar SCAN: {e}")
        return

    if not arquivos:
        return

    print(f"\n{'─'*55}")
    print(f"  Ciclo {datetime.now().strftime('%H:%M:%S')} — {len(arquivos)} arquivo(s)")
    print(f"{'─'*55}")
    for nome in arquivos:
        processar_arquivo(nome)


# ── Ponto de entrada ─────────────────────────────────────────

if __name__ == '__main__':
    configurar_log()
    garantir_estrutura()

    print("\n" + "="*55)
    print("   MN-AutoPorto v4.0  |  DIÁRIO DE BORDO AUTO")
    print(f"   SCAN     : {P_SCAN}")
    print(f"   DEST     : {P_DEST_BASE}")
    print(f"   Relatório: {LOG_CSV}")
    print("   Modo     : Lê PDF → detecta data/turno → arquiva")
    print("   Revisão  : nível MASTER — produção industrial")
    print("="*55)
    print("  Pressione Ctrl+C para encerrar.\n")
    logging.info("MN-AutoPorto v4.0 INICIADO")

    while True:
        try:
            ciclo_varredura()
            time.sleep(INTERVALO_SEGUNDOS)
        except KeyboardInterrupt:
            logging.info("Sistema encerrado pelo operador")
            print("\n[MN] Sistema encerrado. Relatório salvo.\n")
            break
