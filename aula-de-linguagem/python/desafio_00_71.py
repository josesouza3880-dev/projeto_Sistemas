print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Ler nome completo e mostrar: Quantidade de caracteres total Nome em maiúsculas e minúsculas Total de letras (sem espaços) Quantidade de letras do ultimo nome')

nome = input("Digite seu nome completo: ").strip()

# Quantidade de caracteres total (incluindo espaços)
print(f"Quantidade de caracteres total: {len(nome)}")

# Nome em maiúsculas
print(f"Nome em maiúsculas: {nome.upper()}")

# Nome em minúsculas
print(f"Nome em minúsculas: {nome.lower()}")

# Total de letras (sem espaços)
total_letras = len(nome.replace(" ", ""))
print(f"Total de letras (sem espaços): {total_letras}")

# Quantidade de letras do último nome
ultimo_nome = nome.split()[-1]
print(f"Quantidade de letras do último nome: {len(ultimo_nome)}")
