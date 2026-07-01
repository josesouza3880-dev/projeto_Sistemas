print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Multa de velocidade (> 80 km/h → R$ 7 por km acima).')

velocidade = float(input("Digite a velocidade do carro (km/h): "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"Você foi multado! Excedeu {excesso:.0f} km/h.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite. Boa viagem!")
