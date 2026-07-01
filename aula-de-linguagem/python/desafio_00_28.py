print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Alistamento militar (ainda vai, na hora ou já passou).')
print('• Leia o ano de nascimento de um jovem e informe se ele ainda vai se')
print('alistar, se está na hora de se alistar ou se já passou do tempo.')
print('• O programa também deve informar quantos anos faltam ou quantos anos se passaram do prazo.')
import datetime
ano=datetime.date.today().year
nasci=int(input('digite o ano do seu nascimento: '))
idade=ano-nasci
if idade<18:
    faltam=18-idade
    print(f'ainda vai se alistar,faltam {faltam} anos')
elif idade==18:
    print('hora de alistar')
else:
    passaram=idade-18
    print(f'já passou do tempo de alista {passaram} anos')