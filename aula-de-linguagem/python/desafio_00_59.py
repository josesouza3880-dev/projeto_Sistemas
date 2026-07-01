print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:11/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Leia qualquer valor do teclado Mostre: O tipo primitivo As informações obtidas com métodos como .is..')

texto = input('Digite algo: ')

print(texto,'apenas números?', texto.isnumeric())#apenas números?
print(texto,'apenas letras?',texto.isalpha())#apenas letras?
print(texto,'letras e números?',texto.isalnum())#letras e números?
print(texto,'tudo maiúsculo?',texto.isupper())#tudo maiúsculo?
print(texto,'tudo minúsculo?',texto.islower())#tudo minúsculo?
