print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Comparação entre dois números (maior, menor ou iguais).')
print('• Leia dois números inteiros e mostre uma das seguintes mensagens:')
print('• "O primeiro valor é maior"')
print('• "O segundo valor é maior"')
print('• "Não existe valor maior, os dois são iguais"')

num1=int(input('digite o 1º número: '))
num2=int(input('digite o 2º número: '))
if num1>num2:
    print(f'1º número é maior de 2º número')
elif num2>num1:
    print(f'2º número é maior de 1º número')
else:
    print(f'Não existe valor maior, os dois são iguais')