print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Número positivo, negativo ou zero:')
print('• Faça um programa que verifique se um número é positivo, negativo ou zero.')
print('• O programa deve solicitar um número ao usuário e, usando condições aninhadas,')
print('imprimir a informação correspondente.')


num=int(input('digite um número positivo ou negativo: '))
if num >0:
    print('positivo')
elif num<0:
    print('negativo')
else:
    num=0
    print('igual')