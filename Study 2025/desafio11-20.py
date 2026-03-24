# ===== Desafio 11 =====

real = float(input('Quantos reais você tem? '))
dolar = 3.27

print('Com os seus {:.2f} reais você consegue comprar {:.2f} dólares.'.format(real, real / dolar))

# ===== Desafio 12 =====

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
rendimentoTinta = 2

print('Para uma parede de {} metros de altura e {} metros de largura você irá precisar de {} litros de tinta.'.format(altura, largura, area / rendimentoTinta))

# ===== Desafio 13 =====

preco = float(input('Qual o preco do produto? '))
desconto = 5 / 100

print('O preco do produto é de {:.2f} reais e com {} % de desconto ele sairá por {:.2f} reais.'.format(preco, desconto * 100, preco - preco * desconto))

# ===== Desafio 14 =====

salario = float(input('Qual o salário do funcionário? '))
aumento = 15 / 100
salarioLiquido = salario + salario * aumento

print('O salário do funcionário é de {:.2F} reais e com {}% de aumento irá para {:.2f} reais.'.format(salario, aumento * 100, salarioLiquido))

# ===== Desafio 15 =====

celsius = float(input('Qual a temperatura em graus celsius? '))
farenheit = ((9 * celsius) / 5) + 32

print('A temperatura de {:.1f} graus celsius equivale a {:.1f} graus farenheit.'.format(celsius, farenheit))

# ===== Desafio 16 =====

distancia = float(input('Quantos km você percorreu com o carro?'))
tempo = int(input('Quantos dias você ficou com o carro?'))

preco = (tempo * 60) + (distancia * 0.15)

print('Você ficou com o carro por {} dias e percorreu {:.1f} quilômetros. O valor a pagar será de R${:.2f}'.format(tempo, distancia, preco))

# ===== Desafio 17 =====

from math import trunc

num = float(input('Digite um número paras que seja mostrado sua parte inteira: '))
print(trunc(num))

# ===== Desafio 18 =====

import random
from math import pow, sqrt

catetoOposto = random.randint(1, 15)
catetoAdjacente = random.randint(1, 15)
hipotenusa = (pow(catetoOposto, 2) + pow(catetoAdjacente, 2))

print('Um triângulo de cateto oposto {} e cateto adjacente {} sua hipotenusa mede {}'.format(catetoOposto, catetoAdjacente, sqrt(hipotenusa)))

# ===== Desafio 19 =====

import random
import math

angulo = random.randint(1, 360)
convRad = math.radians(angulo)

print('O seno do ângulo {} é {:.4F}, o cosseno é {:.4f} e a tangente é {:.4f}.'.format(angulo, math.sin(convRad), math.cos(convRad), math.tan(convRad)))

# ===== Desafio 20 =====

import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi o {}'.format(random.choice(alunos)))




