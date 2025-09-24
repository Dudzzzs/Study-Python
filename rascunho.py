# ===== Desafio 93 =====

import random

vencedor = {'nome': '', 'dado': 0}
jogador = {}
participantes = []
contador = 1
valores_usados = []

for j in range(0,4):
    jogador['nome'] = input(f'Qual o nome do {contador} jogador? ').title()
    
    while True:
        dado = random.randint(1,6)

        if dado not in valores_usados:
            valores_usados.append(dado)
            jogador['dado'] = dado
            break
    
    contador += 1
    participantes.append(jogador.copy())

for p in participantes:
    if p['dado'] > vencedor['dado']:
        vencedor = p.copy()

for p in participantes:
    print(f'O jogador {p["nome"]} jogou o dado e tirou {p["dado"]}.')

print(f'\033[1;32mO vencedor foi {vencedor["nome"]} que tirou {vencedor["dado"]}.\033[m')



    

