# ===== Desafio 111 =====

import moeda

preco = float(input('Digite o preço do produto: R$'))

print(f'\033[1;33mA metade de R${moeda.formatar(preco)} é R${moeda.metade(preco, form=True)}\033[m')
print(f'\033[1;34mO dobro de R${moeda.formatar(preco)} é R${moeda.dobro(preco)}\033[m')
print(f'\033[1;32mO preço R${moeda.formatar(preco)} acrescido de 10% é R${moeda.aument(preco, form=True)}\033[m')
print(f'\033[1;31mO preço R${moeda.formatar(preco)} reduzido de 5% é R${moeda.reduz(preco)}\033[m')

# ===== Desafio 112 =====

import moeda

preco = float(input('Digite o preço do produto: R$'))
aumento = int(input('Digite a porcentagem de aumento: '))
reducao = int(input('Digite a porcentagem de redução: '))

moeda.resumo(preco, aumento, reducao)

# ===== Desafio 113 =====

from import_modulos.moeda import funcoes

preco = float(input('Digite o preço do produto: R$'))
aumento = int(input('Digite a porcentagem de aumento: '))
reducao = int(input('Digite a porcentagem de redução: '))

funcoes.resumo(preco, aumento, reducao)

# ===== Desafio 114 =====

from import_modulos.moeda import funcoes 
from import_modulos.verificacao import verif

while True:
    preco = input('Digite o preço do produto: R$').replace(',', '.').strip()
    
    if verif.verificacao(preco):
        break
    

aumento = int(input('Digite a porcentagem de aumento: '))
reducao = int(input('Digite a porcentagem de redução: '))

funcoes.resumo(preco, aumento, reducao)

# ===== Desafio 115 =====

while True:
    try: 
        valor = int(input('Digite um valor inteiro: '))
    except KeyboardInterrupt:
        print('\033[1;33mO usuário preferiu não digitar um valor!\033[m')
        break
    except (ValueError, TypeError):
        print('\033[1;31mERRO, DIGITE UM VALOR INTEIRO!\033[m')
    else:
        print(f'O valor digitado foi: {valor}')
        break

# ===== Desafio 116 =====

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[1;31mO SITE NÃO ESTÁ ACESSÍVEL\033[m')
else:
    print('\033[1;32mO SITE ESTÁ ACESSSÍVEL\033[m')

# ===== Desafio 117 =====

from import_modulos.pessoas import pessoas

while True:
    msg = '\033[1;33mMENU PRINCIPAL \033[m'
    tam = len(msg) + 4
    print('=' * tam)
    print(f'       {msg}')
    print()
    print('\033[1;35m1: Cadastrar pessoa; \n2: Exibir pessoas; \n3: Sair do programa.\033[m')
    print('=' * tam)

    opcao = int(input('\033[1;35mOpção: \033[m'))

    if opcao == 3:
        print('\033[1;34mPrograma encerrado!\033[m')
        break
    else:
        pessoas.banco_dados(opcao)