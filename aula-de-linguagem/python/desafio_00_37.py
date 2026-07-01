print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Pergunte se um aluno tem nota ≥ 7 ou fez trabalho extra (se sim, é aprovado).')

nota = float(input('Digite a nota do aluno: ')) 
trabalho_extra = input('Fez trabalho extra? (S/N): ').strip().upper() 
if nota >= 7.0 or trabalho_extra == 'S': 
    print('APROVADO') 
else: print('REPROVADO')
