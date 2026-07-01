#1. Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu perimetro.

# Solicita as dimensões do retângulo ao usuário
#base = float(input('Digite o tamanho da base do retângulo: '))
#altura = float(input('Digite o tamanho da altura do retângulo: '))

# Calcula a área e o perímetro
#area = base * altura
#perimetro = 2 * (base + altura)

#print(f'\nA área do retângulo é: {area}')
#print(f'O perímetro do retângulo é: {perimetro}')

#2. Dado o tamanho do lado de um quadrado, calcular a área e o perimetro do mesmo.

#base = float(input('Digite o tamanho da base do quadrado: '))
#altura = float(input('Digite o tamanho da altura do quadrado: '))

# Calcula a área e o perímetro
#area = base * altura
#perimetro = 2 * (base + altura)

#print(f'\nA área do quadrado é: {area}')
#print(f'O perímetro do quadrado é: {perimetro}')

#3. Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma.
import math

# Solicita o raio da circunferência ao usuário
raio = float(input('Digite o tamanho do raio da circunferência: '))

# Calcula a área e o perímetro (circunferência)
# Fórmula da Área: π * raio²
area_circunferencia = math.pi * (raio ** 2)
# Fórmula do Perímetro: 2 * π * raio
perimetro_circunferencia = 2 * math.pi * raio

# Exibe os resultados formatados com 2 casas decimais
print(f'\nA área da circunferência é: {area_circunferencia:.2f}')
print(f'O perímetro da circunferência é: {perimetro_circunferencia:.2f}')