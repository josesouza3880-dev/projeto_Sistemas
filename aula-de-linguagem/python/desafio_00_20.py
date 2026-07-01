print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Verificar se três retas podem formar um triângulo.')

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

print(f"Testando se {r1}, {r2} e {r3} podem formar um triângulo...")

if r1 < r2 + r3:
    if r2 < r1 + r3:
        if r3 < r1 + r2:
            print(" SIM! Esses valores podem formar um triângulo.")
        else:
            print(" NÃO! O lado 3 é muito grande.")
    else:
        print(" NÃO! O lado 2 é muito grande.")
else:
    print(" NÃO! O lado 1 é muito grande.")
