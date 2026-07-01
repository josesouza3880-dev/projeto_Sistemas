print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:: Cálculo de IMC com classificação.')
print('• Leia o peso e a altura de uma pessoa e calcule o IMC.')
print('• Informe o status da pessoa com base na tabela:')
print('•Entre 18.5 e 25: Peso ideal')
print('•Entre 25 e 30: Sobrepeso')
print('Entre 30 e 40: Obesidade')
print('Acima de 40: Obesidade mórbida')
print('-'*20)
#Cálculo de IMC com classificação.
#• Leia o peso e a altura de uma pessoa e calcule o IMC.
# Informe o status da pessoa com base na tabela:
#Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
#Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
print('Cálculo de IMC com classificação')
print('Abaixo de 18.5: Abaixo do peso')
print('Entre 18.5 e 25: Peso ideal')
print('Entre 25 e 30: Sobrepeso')
print('Entre 30 e 40: Obesidade')
print('Acima de 40: Obesidade mórbida')
print('-'*20)
peso=float(input('digite seu peso: '))
altura=float(input('digite sua altura: '))

imc = peso / (altura ** 2)  # Fórmula correta!
print(f'calculo {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')