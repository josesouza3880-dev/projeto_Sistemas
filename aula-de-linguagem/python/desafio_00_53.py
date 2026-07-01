Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome='Bruna'
>>> print (nome)
Bruna
>>> nome='Paulo Pigoso'
>>> print(nome)
Paulo Pigoso
>>> print('nome:',nome)
nome: Paulo Pigoso
>>> nome=imput("qual o seu nome? ")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nome=imput("qual o seu nome? ")
NameError: name 'imput' is not defined. Did you mean: 'input'?
>>> nome=input('qual seu nome? ')
qual seu nome? 
>>> nome=input('45','kilos')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    nome=input('45','kilos')
TypeError: input expected at most 1 argument, got 2
>>> nome=input('quantos anos você tem? ')
quantos anos você tem? 
>>> nome=input('qual seu peso? ')
qual seu peso? 
>>> numbers=[1,2,3,4,5]
>>> soma=ford(lambda acc, x: acc + x, 0, numbers)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    soma=ford(lambda acc, x: acc + x, 0, numbers)
NameError: name 'ford' is not defined. Did you mean: 'ord'?
