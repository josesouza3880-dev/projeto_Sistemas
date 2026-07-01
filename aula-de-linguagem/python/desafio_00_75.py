print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Ler frase e mostrar: Quantas vezes aparece a letra ‘A’ Posição da primeira ocorrência Posição da última ocorrência.')

frase = input("Digite um nome:\n").strip().upper()

print(f"Quantidade de 'A' no nome: {frase.count('A')}")
print(f"Quantidade de 'A' entre índices 0 e 9: {frase.count('A', 0, 10)}")

