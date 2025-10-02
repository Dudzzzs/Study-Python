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

