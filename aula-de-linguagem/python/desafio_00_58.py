from datetime import date
atual=date.today().year
maiores=0
menores=0
for pessoa in range(1,8):
    nasci=int(input(f'ano de nascimento {pessoa}ª pessoa: ') )
idade=atual-nasci
if idade>=21:
    maiores+=1
else:
    menores+=1

print(f'maiores de idade:{maiores}')
print(f'menores de idade:{menores}')