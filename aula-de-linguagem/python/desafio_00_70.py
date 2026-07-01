print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Ordem de Apresentação Sorteie a ordem de apresentação de 4 alunos..')
import random

# Lendo o nome dos alunos
aluno1 = input("Digite o nome do 1º aluno: ")
aluno2 = input("Digite o nome do 2º aluno: ")
aluno3 = input("Digite o nome do 3º aluno: ")
aluno4 = input("Digite o nome do 4º aluno: ")

# Criando a lista
lista = [aluno1 , aluno2 , aluno3 , aluno4 ]

# Embaralhando a ordem
random.random(lista)

# Exibindo o resultado
print("A ordem de apresentação será:")
print(lista)
