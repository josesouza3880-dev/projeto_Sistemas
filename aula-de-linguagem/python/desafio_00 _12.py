print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Compare dois nomes e informe qual vem primeiro na ordem alfabética.')


nom1=input('digite o nome 2º: ').strip().title()
nom=input('digite o mome 1º: ').strip().title()
if nom>nom1:
    print(f'o nome 1º {nom} , o 2º {nom1} ')
else:
    nom<nom1
    print(f'o nome 2º {nom1} , o 1º {nom} ')