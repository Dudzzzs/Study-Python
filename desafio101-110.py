# ===== Desafio 101 =====

import random

sorteados = []
pares = []

def sorteio(sort):
    print('Sorteando 5 números: ', end='')
    for c in range(0,5):
        num = random.randint(1, 100)
        print(f'{num} ', end='')
        sort.append(num)
    print()

def par(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
            soma += n
    print(f'Os números pares sorteados foram {pares} e a soma deles é: {soma}')

sorteio(sorteados)
par(sorteados)

# ===== Desafio 102 =====

import random

sorteados = []
pares = []

def sorteio(sort):
    print('Sorteando 5 números: ', end='')
    for c in range(0,5):
        num = random.randint(1, 100)
        print(f'{num} ', end='')
        sort.append(num)
    print()

def par(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
            soma += n
    print(f'Os números pares sorteados foram {pares} e a soma deles é: {soma}')

sorteio(sorteados)
par(sorteados)

