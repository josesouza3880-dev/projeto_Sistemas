print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:: Gerenciador de pagamentos (descontos e juros).')
print('• Leia o preço de um produto e a condição de pagamento.')
print('• Calcule o valor a ser pago com base nas seguintes condições:')
print('• À vista (dinheiro/cheque): 10% de desconto')
print('• À vista no cartão: 5% de desconto')
print('Em até 2x no cartão: Preço normal')
print('3x ou mais no cartão: 20% de juros')
print('-'*20)


preco = float(input("Preço do produto: R$ ")) 

print("[1] À vista dinheiro/cheque: 10% de desconto ")
print('[2] À vista no cartão: 5% de desconto')
print('[3] Em até 2x no cartão: preço normal' )
print("[4] 3x ou mais no cartão: 20% de juros ") 


opcao = int(input('Escolha a opção: '))


if opcao == 1:
    total = preco - (preco * 0.10) 
    print(f'o preço e,{total}')
elif opcao == 2: 
    total = preco - (preco * 0.05) 
    print(f'a vista é {total}')
elif opcao == 3: 
    total = preco 
    parcela = total / 2 
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f}')
elif opcao == 4: 
    total = preco + (preco * 0.20) 
    parcelas = int(input('Quantas parcelas? ')) 
    valor_parcela = total / parcelas 
    print(f'Sua compra será parcelada em {parcelas}x de R$ {valor_parcela:.2f}') 
else: 
    total = preco 
    print('Opção inválida!') 
    print(f'Total a pagar: R$ {total:.2f}')
