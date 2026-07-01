print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Aprovado na disciplina:O aluno é aprovado se tiver média ≥ 7ou média entre 5 e 6,9 com frequência')


media = float(input('Digite a média do aluno: ')) 
frequencia = float(input('Digite a frequência (%): ')) 
if media >= 7.0: print('APROVADO') 
elif media >= 5.0 and frequencia >= 75: 
    print('APROVADO COM RECUPERAÇÃO') 
else: print('REPROVADO')
