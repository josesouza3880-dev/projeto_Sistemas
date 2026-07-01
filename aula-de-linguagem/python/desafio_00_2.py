aluno={
    'nome':'Ana',
    'idade':20,
    'curso':'python'
}
aluno['nota']=9.5
aluno['idade']=21

aluno.pop('nota')#remove 
del aluno['curso']
print(aluno)

print(aluno.keys())#retorna todas as chaves
print(aluno.values())#retorna todos os valores
print(aluno.items())#retorna os pares chave:valor



'''
#usar for para percorrer chaves e valores
for chave,valor in aluno.items():
    print(f'{chave}>{valor}')
    '''
aluno2=aluno.copy()
aluno2=['nome']='pedro'
print(aluno)
print(aluno2)