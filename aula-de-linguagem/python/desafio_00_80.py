Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> idade = 18
>>> peso = 44,4
>>> print ('seu peso e idade')
seu peso e idade
>>> print(idade,peso)
18 (44, 4)
>>> nome =josé
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nome =josé
NameError: name 'josé' is not defined
>>> nome = josé
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nome = josé
NameError: name 'josé' is not defined
>>> nome = luiz
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    nome = luiz
NameError: name 'luiz' is not defined
>>> print('seu', peso ,'e', idade)
seu (44, 4) e 18
>>> nome = (josé)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    nome = (josé)
NameError: name 'josé' is not defined
>>> nome = 'josé'
>>> idade = 18
>>> peso = 44,4
>>> print('O seu nome', nome , ' tem idade ', idade, ' o peso de um saco de cimento',peso)
O seu nome josé  tem idade  18  o peso de um saco de cimento (44, 4)
>>> nome = input('Escreva seu nome: ')
Escreva seu nome: cleide sem calcinha
>>> nome= nome
>>> print('escreva' nome)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> nome = input('qual é seu peso')
qual é seu peso 900000000000000000000
>>> nome == input(' luis ou com z são cornos' )
