print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Aprovação de empréstimo (prestação ≤ 30% do salário).')
print('• Crie um programa que aprova ou nega um empréstimo bancário para a compra de uma casa')
print('• Ele deve perguntar o valor da casa,')
print('• o salário do comprador')
print('• em quantos anos ele irá pagar.')
print('• Calcule o valor da prestação mensal e verifique se ele excede 30% do salário. Se exceder, o empréstimo deve ser negado')

valor_casa = float(input('Digite o valor da casa: R$ ')) 
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))
meses = anos * 12 
presta = valor_casa / meses 
if presta <= salario * 0.30:
     print(f'Empréstimo APROVADO! A prestação será de R$ {presta:.2f} por mês.')
else:
     print(f'Empréstimo NEGADO! A prestação de R$ {presta:.2f} excede 30% do salário.')