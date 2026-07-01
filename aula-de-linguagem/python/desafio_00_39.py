print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Promoção de loja: O cliente tem direito ao desconto se: Comprou acima de R$ 100, OU comprou acima de R$ 50 e é cliente VIP.')
valor_compra = float(input('Digite o valor da compra: R$ ')) 
cliente_vip = input('É cliente VIP? (S/N): ').strip().upper()
if valor_compra > 100 or (valor_compra > 50 and cliente_vip == 'S'):
    print('Desconto aplicado!')
else: 
    print('Sem direito a desconto.')


