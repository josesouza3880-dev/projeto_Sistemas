print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:: Jogo da adivinhação (número de 0 a 5).')

from random import randint
comp=randint(0,5)
print('\n')
print('eu estou escolhendo um número de 0 a 5 ...boa sorte!')
print('\n')
n=int(input('o número da sote foi...'))
print(" ")
if n==comp:
    print('que legal tem sorte mesmo')
else:
    print(f"errou,o número que escolhir foi {comp} e não foi {n}")