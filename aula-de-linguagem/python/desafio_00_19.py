print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:: Calcular aumento salarial (≤ R$ 1.250 → 15%; senão 10%).')
salario = float(input("Digite o salário atual: R$ "))

if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)

print(f"O novo salário é: R$ {novo_salario:.2f}")
