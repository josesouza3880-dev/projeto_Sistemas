print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:11/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Hipotenusa Leia catetos e calcule a hipotenusa de um triângulo retângulo.')

import math
co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir: {hi:.2f}')