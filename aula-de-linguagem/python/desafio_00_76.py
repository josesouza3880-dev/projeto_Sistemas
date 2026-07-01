print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Ler nome completo e mostrar: Primeiro e último nome separadamente Ex.: "Ana Maria de Souza" → "Ana" e "Souza".')

nome = input("Digite seu nome: ").strip().title()
n=nome.split()
print(f"nome {nome}; primeiro:nome {n[0]} e último nome {n[-1]}")

