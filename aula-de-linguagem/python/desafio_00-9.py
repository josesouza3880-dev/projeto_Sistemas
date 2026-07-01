#permitem organizar dados mais complexos
'''
turma=[
    {'nome':'Ana','nota':9},
    {'nome':'Pedro','nota':8}
]

for aluno in turma:
    print(aluno['nome'],aluno['nota']),

    if 'nota'in aluno:
        print(aluno['nota']),
    else:
        print('nota nao encontrado')

aluno.update({'nota':9.5,'curso':'engemharia'})
print(aluno)

aluno2=aluno.copy()
aluno2=['nome']='pedro'
print(aluno)
print(aluno2)
'''
alunos=[
    {'nome':'ana','idade':20,'nota':9.0},
    {'nome':'pedro','idade':22,'nota':7.5}
]
alunos.append({'nome':'mariana','idade':19,'nota':8.3})
print(alunos)
alunos=[alunos for alunos in alunos if alunos['nome']!='ana']
print(alunos)