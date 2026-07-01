print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE:Cinema v2.0 – Proibir menor de 12 desacompanhado')
print('• Adicione uma verificação para a entrada de:')
print('▪ • "menor desacompanhado".')
print('▪• Se a idade for menor que 12 anos,')
print('▪• informe que a entrada só é permitida com um responsável.')


idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Não pode assistir (menor de 12).')
elif idade == 12:
    print('Precisa de autorização pra entrar.')
elif idade >= 18:
    print('Você pode entrar!')
else:
    print('Permitido, mas com restrições.')

alt = input('Está desacompanhado? (sim/não)\n').strip().lower()

if alt == 'sim':
    print('Entrada só permitida com um responsável.')
elif alt == 'não':
    print('Pode entrar se tiver 12 anos ou mais e acompanhado.')
else:
    print('Resposta inválida.')
