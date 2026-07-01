print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:  Média do aluno (aprovado, recuperação, reprovado).')
print('• Leia 4 notas de um aluno e calcule a média.')
print('• Informe a situação do aluno com base na média:')
print('• Média abaixo de 5.0: REPROVADO')
print('• Média abaixo 7.0: RECUPERAÇÃO')
print('• Média 7.0 ou superior: APROVADO')
('\n')

soma=0 

soma1=float(input(' digite a 1º nota do aluno: '))

soma2=float(input(' digite a 2º nota do aluno: '))

soma3=float(input(' digite a 3º nota do aluno: '))

soma4=float(input(' digite a 4º nota do aluno: '))

media=(soma1+soma2+soma3+soma4)/4

if media<5.0:

    print(f'reprovado cpm a média {media}')

elif media<7.0:

    print(f'em recuperção com a média {media}')

else:

    print(f'você passou com a média {media}')