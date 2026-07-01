print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Classificação de nadadores por idade.')
print('• Leia o ano de nascimento de um atleta e classifique-o em uma')
print('categoria de natação de acordo com a idade:')
print('• Até 9 anos: MIRIM')
print('• Até 14 anos: INFANTIL')
print('• Até 19 anos: JÚNIOR')
print('• Até 25 anos: SÊNIOR')
print('• Acima de 25 anos: MASTER')

import datetime
ano=datetime.date.today().year
nas=int(input('digite seu nascimeno: '))
idade=ano-nas
if idade<=9:
    print('mirim')
elif idade<=14:
    print('infantil')
elif idade<=19:
    print('júnior')
elif idade<=25:
    print('sênior')
else:
    print('master')