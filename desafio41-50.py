# ===== Desafio 41 =====

nasc = int(input('Qual seu ano de nascimento? '))
idade = 2025 - nasc

if idade < 18:
    tempo = 18 - idade
    print('Faltam {} anos para você se alistar.'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Já se passaram {} anos do seu tempo de alistamento.'.format(tempo))
else:
    print('Está na sua época de alistamento.')

# ===== Desafio 42 =====

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi de {:.1F} e por isso você foi REPROVADO.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi de {:.1F} e por isso você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua média foi de {:.1F} e por isso você foi APROVADO.'.format(media))

# ===== Desafio 43 =====

nasc = int(input('Qual seu ano de nascimento? '))
idade = 2025 - nasc

if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade > 15 and idade <= 19:
    print('Você tem {} anos e sua categoria é JÚNIOR.'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER.'.format(idade))

# ===== Desafio 44 =====

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
triangulo = str

if r1 == r2 and r2 == r3:
    triangulo = 'equilátero'
elif r1 == r2 or r2 == r3 or r1 == r3:
    triangulo = 'isósceles'
elif r1 != r2 and r1 != r3 and r2 != r3:
    triangulo = 'escaleno'


if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Com essas 3 retas de comprimento {}, {} e {} você pode formar um triângulo {}!'.format(r1, r2, r3, triangulo))
else:
    print('Com essas 3 retas de comprimento {}, {} e {} você não pode formar um triângulo!'.format(r1, r2, r3))

# ===== Desafio 45 =====

peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura atual: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu imc é de {:.2f}kg/m2 e por isso você está ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é de {:.2f}kg/m2 e por isso você está no PESO IDEAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é de {:.2f}kg/m2 e por isso você está SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é de {:.2f}kg/m2 e por isso você está na OBESIDADE.'.format(imc))
else:
    print('Seu imc é de {:.2f}kg/m2 e por isso você está na OBESIDADE MÓRBIDA.'.format(imc))

# ===== Desafio 46 =====

import random

preco = random.randint(1,100)

print('O preço do produto é \033[1;31mR${}\033[m'.format(preco))

print('Qual será a forma de pagamento? \n1 - A vista no dinheiro ou cheque; \n2 - A vista no cartão; \n3 - Cartão de 2x; \n4 - Cartão de 3x ou mais.' )
pagamento = int(input('Escolha a forma de apagamento: '))

if pagamento == 1:
    preco = preco - (preco * (10 / 100))
    print('Para pagamento a vista em dinheiro ou cheque temos 10% de desconto e com isso o valor do produto será R${:.2f}'.format(preco))
elif pagamento == 2:
    preco = preco - (preco * (5 / 100))
    print('Para pagamento a vista no cartão temos 5% de desconto e com isso o valor do produto será R${:.2f}'.format(preco))
elif pagamento == 3:
    print('Para pagamento no cartão até 2x não temos desconto e com isso o valor do produto será R${:.2f}'.format(preco))
elif pagamento == 4:
    preco = preco + (preco * (20 / 100))
    print('Para pagamento no cartão de 3x ou mais temos 20% de juros e com isso o valor do produto será R${:.2f}'.format(preco))
else:
    print('Opção inválida!')

# ===== Desafio 47 =====

import random

print('\033[1;33mVamos jogar JOKENPÔ!\033[m')

computadorJogada = random.choice(['pedra', 'papel', 'tesoura'])
minhaJogada = input('Você quer pedra, papel ou tesoura? ')

if computadorJogada == 'tesoura' and minhaJogada == 'papel':
    print('O computador jogou {} e você {}. COMPUTADOR VENCE!'.format(computadorJogada, minhaJogada))
elif computadorJogada == 'tesoura' and minhaJogada == 'pedra':
    print('O computador jogou {} e você {}. VOCÊ VENCE!'.format(computadorJogada, minhaJogada))
elif computadorJogada == 'papel' and minhaJogada == 'pedra':
    print('O computador jogou {} e você {}. COMPUTADOR VENCE!'.format(computadorJogada, minhaJogada))
elif computadorJogada == 'papel' and minhaJogada == 'tesoura':
    print('O computador jogou {} e você {}. VOCÊ VENCE!'.format(computadorJogada, minhaJogada))
elif computadorJogada == 'pedra' and minhaJogada == 'papel':
    print('O computador jogou {} e você {}. VOCÊ VENCE!'.format(computadorJogada, minhaJogada))
elif computadorJogada == 'pedra' and minhaJogada == 'tesoura':
    print('O computador jogou {} e você {}. COMPUTADOR VENCE!'.format(computadorJogada, minhaJogada))
elif computadorJogada == minhaJogada:
    print('O computador jogou {} e você {}. EMPATE!'.format(computadorJogada, minhaJogada))
else:
    print('Você não sabe jogar!')

# ===== Desafio 48 =====

import time

for c in range(10, 0, -1):
    print('Faltam {} segundos...'.format(c))
    time.sleep(1)
print('\033[1;32mFELIZ ANO NOVO!!\033[m')

# ===== Desafio 49 =====

contador = 0
pares = []

for c in range(1, 51, 1):
    if c % 2 == 0:
        pares.append(c)
        contador = contador + 1
print('Os pares entre 1 e 50 são {}'.format(pares))

# ===== Desafio 50 =====

soma = 0

for c in range(1, 501, 1):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
print('A soma dos números ímpares e múltiplos de 3 entre 1 e 500 é: {}'.format(soma))



