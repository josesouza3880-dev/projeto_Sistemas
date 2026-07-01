# Conversor de bases numéricas
print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:D041: Conversor de bases numéricas (binário, octal, hexadecimal)• Leia um número inteiro e permita ao usuário escolher a base deconversão (binário, octal ou hexadecimal).• Converta o número para a base escolhida.')






num = int(input("Digite um número inteiro: "))

print("""
Escolha a base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
""")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} convertido para BINÁRIO é {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para OCTAL é {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para HEXADECIMAL é {hex(num)[2:]}")
else:
    print("Opção inválida! Tente novamente.")
