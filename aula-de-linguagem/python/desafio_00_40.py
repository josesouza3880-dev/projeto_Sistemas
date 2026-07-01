print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Promoção de loja: O cliente tem direito ao desconto se: Comprou acima de R$ 100, OU comprou acima de R$ 50 e é cliente VIP.')

idade = int(input('Digite a idade do paciente: ')) 
febre = input('Está com febre? (S/N): ').strip().upper() 
pressao_alta = input('Pressão alta? (S/N): ').strip().upper() 
if idade < 12 or idade > 65 or (febre == 'S' and pressao_alta == 'S'):
     print('PACIENTE URGENTE') 
else: 
     print('PACIENTE NÃO URGENTE')
