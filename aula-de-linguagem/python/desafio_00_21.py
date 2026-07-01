print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Situação do aluno: Calcular a média de 3 notas, para status de Aprovado média no mínimo 7.0, caso contrario Reprovado')

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) /3 

print(f"Média: {media:.2f}")
if media >= 7.0:
    print("Situação: Aprovado ")
else:
    print("Situação: Reprovado ")










