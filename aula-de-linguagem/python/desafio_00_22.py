print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:: Saudações personalizadas por nome:▪ Crie um programa que pergunte o nome do usuário.▪ O programa deve ter diferentes saudações dependendo do nome inserido.▪ Utilize if para um nome específico (ex: “Neymar"),▪ elif para uma lista de nomes comuns, e else para todos os outros nomes.')

nome = input("Qual é o seu nome? \n").strip().title()

if nome == "Sophia":
    print("A mulher mais bonita ")

elif nome == "João" or nome == "Maria" or nome == "Ana" or nome == "Pedro" or nome == "Luiz":
    print(f"Olá {nome}, seja bem-vindo(a)! ")

else:
    print(f"Prazer em conhecer você, {nome}! ")


