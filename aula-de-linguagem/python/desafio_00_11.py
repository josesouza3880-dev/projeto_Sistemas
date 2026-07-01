print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE::Peça dois números ao usuário e exiba se são iguais ou diferentes.')

num=int(input('digite o número 1º: '))
num1=int(input('digite o  número 2º: '))
if num>num1:
    print(f'o valor do 1º {num} é maior, o 2º {num1} é menor')
elif num<num1:
    print(f'o valor do 2º {num1} é maior, o 1º {num} é menor')
else:
    num=num1
    print('são iguais')