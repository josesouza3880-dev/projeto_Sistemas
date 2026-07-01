print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:13/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Entrada no cinema por idade (maior de 18, autorização, não permitido).')
print('▪ Desenvolva um programa que simule a verificação de idade para entrar em um cinema.')
print('▪ Ele deve pedir a idade do usuário e verificar se ele pode assistir ao filme')
print('▪ (maior de 18 anos) ou se precisa de autorização (entre 12 e 18 anos).')
print('▪ Use else para indicar que ele não pode assisti')

idade=int(input('Quantos anos você tem ? \n'))
if idade>18:
           print('você é maior de idade')
elif idade >=12:
           print('precisa de autorização  pra entra')
else:
          print('não pode assisti(menor de 12)')