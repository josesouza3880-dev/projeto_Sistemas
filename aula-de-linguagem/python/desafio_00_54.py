#frase ='Curso python básico'#(tem indice 19,e tem 18 letras)
#print(len(frase))
#print(frase[6:12])
#print(frase[:5])
#print(frase[:9])
#print(frase[6:11])
#print(frase[6:])
#print(frase[6:19:2])
#print(frase.count('o'))
#print(frase.count('o',0,10))
#print(frase.find('básico'))
#print(frase.find('Java'))
#print('curso'in frase)#FALSE
#print('Curso'in frase)#true
#print(frase.replace('python','Android'))#ele troca de frase
#print(frase.upper())#todos maiúsculo
#print(frase.lower())#todos minúscula
#print(frase.capitalize())#letra maiúscula e restante minúsculo
#print(frase.title())#primeira letra de cada palavra maiúdcula
#print('   Curso python básico'.strip())#remove espaços do início do fim
#print('Curso python básico'.rstrip())#remove espaço direito
#print('Curso python básico'.lstrip())#remove espaço esquerdo
#print(frase.split())#divide a string em uma lista de palavras(separado)
#lista=['curso','python','básico']#junta elementode uma única string,usando o separador
#print('-'join.(lista))#separador

frase = 'Curso python básico'  # índice vai de 0 a 18 (19 caracteres no total, incluindo espaços)

print(f"Tamanho da string: {len(frase)}")

print(f"Caracteres do índice 6 ao 11: {frase[6:12]}")
print(f"Do início até o índice 4: {frase[:5]}")
print(f"Do início até o índice 8: {frase[:9]}")
print(f"Do índice 6 ao 10: {frase[6:11]}")
print(f"Do índice 6 até o final: {frase[6:]}")
print(f"Do índice 6 até 18, pulando de 2 em 2: {frase[6:19:2]}")

print(f"Quantidade de 'o' na frase: {frase.count('o')}")
print(f"Quantidade de 'o' entre índices 0 e 9: {frase.count('o', 0, 10)}")

print(f"Posição onde começa 'básico': {frase.find('básico')}")
print(f"Tentando encontrar 'Java' (retorna -1 se não existe): {frase.find('Java')}")

print(f"Existe 'curso' na frase? {'curso' in frase}")
print(f"Existe 'Curso' na frase? {'Curso' in frase}")

print(f"Substituindo 'python' por 'Android': {frase.replace('python', 'Android')}")

print(f"Tudo maiúsculo: {frase.upper()}")
print(f"Tudo minúsculo: {frase.lower()}")
print(f"Primeira letra maiúscula, resto minúsculo: {frase.capitalize()}")
print(f"Primeira letra de cada palavra maiúscula: {frase.title()}")

print(f"Removendo espaços dos dois lados: {'   Curso python básico   '.strip()}")
print(f"Removendo espaços da direita: {'Curso python básico   '.rstrip()}")
print(f"Removendo espaços da esquerda: {'   Curso python básico'.lstrip()}")

print(f"Transformando a frase em lista de palavras: {frase.split()}")

lista = ['curso', 'python', 'básico']
print(f"Juntando os elementos da lista com '-': {'-'.join(lista)}")
