print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Ler número (0 a 9999) e exibir cada dígito separadamente (unidade, dezena, centena, milhar).')

num = int(input("Digite número (0 a 9999): ").strip())

unidade = num % 10
dezena  = (num // 10) % 10
centena = (num // 100) % 10
milhar  = (num // 1000) % 10

print(f"unidade: {unidade}")
print(f"dezena: {dezena}")
print(f"centena: {centena}")
print(f"milhar: {milhar}")



