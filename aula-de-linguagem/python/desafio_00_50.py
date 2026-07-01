#if=se
#elif=senao se
#else=nao
#if opção:
#ação 1
#elif opção2
#ação 2
#else:
#ação 3
#exemplo:ef,elif,else em python
#print('Classificação da idade ')
#idade=int(input('Quantos anos você tem ? \n'))
#if idade<11:
 #    print('você é criança')
#elif  idade>18:
 #    print('você é adolescente') 
#elif idade<60:
 #    print('você é adulto')
#else:
 #    print('você é idoso')
idade=int(input('Quantos anos você tem ? \n'))
if idade<18:
     if idade<=10:
           print('você é criança')
     elif idade<=15:
           print('você é pré adolescente')
     elif idade<60:
           print('você é adulto')
else:
      print('você é adolescente')