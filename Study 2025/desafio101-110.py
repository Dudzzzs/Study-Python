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

# ===== Desafio 103 =====

def voto(idade):
    resultado = ''
    idade = 2025 - ano_nasc

    if idade < 16:
        resultado = 'PROIBIDO'
    elif idade >= 16 and idade < 18:
        resultado = 'OPCIONAL'
    else:
        resultado = 'OBRIGATÓRIO'
    
    return resultado

ano_nasc = int(input('Digite seu ano de nascimento: '))

print(f'Você tem {2025 - ano_nasc} anos e seu voto é {voto(ano_nasc)}.')

# ===== Desafio 104 =====

def fatorial(numero, show=False):
    f = 1
    
    for c in range(numero, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        
        f *= c

    return f

numero = int(input('Digite um número para descobrir seu fatorial: '))
print(fatorial(numero, show=False))

# ===== Desafio 105 =====

def ficha(nome=0, gols=0):
    if nome == 0:
        nome = 'Jogador desconhecido'
        
    print(f'{'=' *5} FICHA DE JOGADOR {'=' *5}')
    print(f'{nome}: {gols} gols')
    print('=' * 28)

nome = input('Digite o nome do jogador: ')
gols = int(input('Quantos gols ele fez? '))
ficha(gols=gols)

# ===== Desafio 106 =====

def leiaInt(resp):
    
    ok = False
    valor = 0

    while ok == False:
        n = str(input(resp))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else: 
            print('\033[1;31mERRO, DIGITE UM NÚMERO!\033[m')
    
    return valor

n = leiaInt('Digite um número: ')
print(f'\033[1;32mVOCÊ DIGITOU O NÚMERO {n}')

# ===== Desafio 107 =====

def notas(*nota):
    """
    -> Função que recebe várias notas e calcula:
    - Quantidade de notas;
    - Maior nota;
    - Menor nota;
    - Média das notas;
    - Situação da turma com base na média.
    """

    resultado = {}
    soma_nota = 0
    conta_nota = len(nota)
    maior_nota = 0
    menor_nota = 0
    media_nota = 0
    situacao = ''

    resultado['Quantidade de notas'] = conta_nota

    for n in nota:
        if n > maior_nota:
            maior_nota = n
        if menor_nota == 0:
            menor_nota = n
        elif n < menor_nota:
            menor_nota = n
        soma_nota += n
    
    resultado['Maior nota'] = maior_nota
    resultado['Menor nota'] = menor_nota

    media_nota = soma_nota / conta_nota
    resultado['Média das notas'] = media_nota

    if media_nota < 7:
        situacao = 'Ruim'
    elif media_nota == 7:
        situacao = 'Mediana'
    else:
        situacao = 'Boa'
    
    resultado['Situação'] = situacao

    return resultado

help(notas)
print(notas(3, 4.5, 10, 7, 8, 1.4, 6))

# ===== Desafio 108 =====

def pyHelp():
    while True: 
        msg = 'Sistema de ajuda Python'
        tam = len(msg) + 4
        print('\033[7;40m=\033[m' * tam)
        print(f'\033[7;40m  {msg}  \033[m')
        print('\033[7;40m=\033[m' * tam)
        
        comando = input('Digite o comando que deseja receber aprender sobre seu funcionamento: (FIM = Encerrar) ')

        if comando == 'FIM':
            print('\033[1;31mPrograma encerrado!!\033[m')
            break
        else:
            help(comando)
           
pyHelp()

# ===== Desafio 109 =====

import moeda

preco = float(input('Digite o preço do produto: R$'))

print(f'\033[1;33mA metade de R${preco:.2f} é R${moeda.metade(preco):.2f}\033[m')
print(f'\033[1;34mO dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}\033[m')
print(f'\033[1;32mO preço R${preco:.2f} acrescido de 10% é R${moeda.aument(preco):.2f}\033[m')
print(f'\033[1;31mO preço R${preco:.2f} reduzido de 5% é R${moeda.reduz(preco):.2f}\033[m')

# ===== Desafio 110 =====

import moeda

preco = float(input('Digite o preço do produto: R$'))

print(f'\033[1;33mA metade de R${moeda.formatar(preco)} é R${moeda.formatar(moeda.metade(preco))}\033[m')
print(f'\033[1;34mO dobro de R${moeda.formatar(preco)} é R${moeda.formatar(moeda.dobro(preco))}\033[m')
print(f'\033[1;32mO preço R${moeda.formatar(preco)} acrescido de 10% é R${moeda.formatar(moeda.aument(preco))}\033[m')
print(f'\033[1;31mO preço R${moeda.formatar(preco)} reduzido de 5% é R${moeda.formatar(moeda.reduz(preco))}\033[m')
