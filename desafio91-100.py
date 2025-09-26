# ===== Desafio 91 =====

aluno = []
sala = []

while True:
    aluno.clear()

    nome = input('Digite o nome do aluno: ').title()
    aluno.append(nome)
    nota1 = float(input('Digite a nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Digite a nota 2: '))
    aluno.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(media)

    sala.append(aluno[:])

    opcao = input('Deseja continuar? [S/N] ').upper()

    if opcao == 'N':
        break

print(f'\033[1;33mAluno | Nome | Nota 1 | Nota 2 | Média\033[m')
print('-=' * 20)

for c in range(0, len(sala)):
    print(f'{c + 1:^5} | {sala[c][0]:^5} | {sala[c][1]:^5} | {sala[c][2]:^5} | {sala[c][3]:^5}')

while True:
    a = int(input('Deseja mostrar a nota de qual aluno? (0 interrompe) '))

    if a == 0:
        break
    elif a - 1 > len(sala):
        print('Esse aluno não existe!')
    else:
        print(f'{a:^5} | {sala[a - 1][0]:^5} | {sala[a - 1][1]:^5} | {sala[a - 1][2]:^5} | {sala[a - 1][3]:^5}')

    if a == 0:
        break
        
print('\033[1;31mPrograma finalizado!\033[m')

# ===== Desafio 92 =====

aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ').title()
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

print(f'O aluno {aluno["nome"]} teve uma média de {aluno["media"]} pontos e está {aluno["situacao"]}.')

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

# ===== Desafio 94 =====

trabalhador = {}

trabalhador['nome'] = input('Qual o seu nome? ').title()
ano_nasc = int(input(f'Qual o ano de nascimento de {trabalhador["nome"]}? '))
trabalhador['idade'] = 2025 - ano_nasc
trabalhador['ctps'] = int(input(f'Digite o número da CTPS de {trabalhador["nome"]} (0 = não tem) '))

if trabalhador['ctps'] != 0:
    trabalhador['contrat'] = int(input(f'Qual foi o ano de contratação de {trabalhador["nome"]}? '))
    trabalhador['salario'] = int(input(f'Qual o salário de {trabalhador["nome"]}? R$'))

    contribuicao = 35 - (2025 - trabalhador['contrat'])
    trabalhador['aposent'] = trabalhador['idade'] + contribuicao

    print(f'\033[1;32mO trabalhador {trabalhador["nome"]} de {trabalhador["idade"]} anos foi contratado em {trabalhador["contrat"]} recebendo R${trabalhador["salario"]} com a CTPS N{trabalhador["ctps"]}. Sua aposentadoria será com {trabalhador["aposent"]} anos.\033[m')
else:
    print(f'\033[1;31m{trabalhador["nome"]} tem {trabalhador["idade"]} anos e ainda não tem CTPS.\033[m')

# ===== Desafio 95 =====

import time

jogador = {}
total_gols = 0
conta_partida = 0

jogador['nome'] = input('Digite o nome do jogador: ').title()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou nesse campeonato? '))

for p in range(0, jogador['partidas']):
    gols = int(input(f'Quantos gols {jogador["nome"]} fez no jogo {conta_partida + 1}? '))
    jogador[f'jogo {conta_partida + 1}'] = gols
    
    conta_partida += 1

    total_gols += gols

jogador['total_gols'] = total_gols

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas nesse campeonato e fez {total_gols} gols, sendo: ')

for j in range(1, jogador['partidas'] + 1):
    print(f'No jogo {j} o {jogador["nome"]} fez {jogador[f'jogo {j}']} gols')
    time.sleep(1)

# ===== Desafio 96 =====

pessoa = {}
galera = []
conta_pessoa = 0
total_idade = 0

while True:
    pessoa['nome'] = input('Qual o nome da pessoa? ').title()
    pessoa['idade'] = int(input(f'Quantos anos {pessoa["nome"]} tem? '))
    pessoa['sexo'] = input(f'Qual o sexo de {pessoa["nome"]}? (M/F) ').upper()

    conta_pessoa += 1
    total_idade += pessoa['idade']

    galera.append(pessoa.copy())

    opcao = input('\033[1;34mDeseja continuar? (S/N) \033[m').upper()

    if opcao == 'N':
        break

media_galera = total_idade / conta_pessoa

print(f'\033[1;32mForam cadastradas {conta_pessoa} pessoas e a media da idade delas é {media_galera:.1f} anos\033[m')

print('\033[1;31mAs mulheres cadastradas foram: \033[m', end='')
for m in galera:
    if m['sexo'] == 'F':
        print(f'\033[1;31m{m['nome']} \033[m', end='')

print()
print(f'\033[1;33mAs pessoas que têm idade maior que a média de {media_galera:.1f} anos são: \033[m', end='')

for p in galera:
    if p['idade'] > media_galera:
        print(f'\033[1;33m{p['nome'] } \033[m', end='')

# ===== Desafio 97 =====

jogador = {}
time = []
total_gols = 0
conta_partida = 0
gols_por_part = []

while True: 
    jogador['nome'] = input('Digite o nome do jogador: ').title()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou nesse campeonato? '))

    for p in range(0, jogador['partidas']):
        gols = int(input(f'Quantos gols {jogador["nome"]} fez no jogo {conta_partida + 1}? '))
        
        gols_por_part.append(gols)
        
        conta_partida += 1

        total_gols += gols
    
    jogador['gols'] = gols_por_part[:]
    jogador['total_gols'] = total_gols
    jogador['total_partidas'] = conta_partida

    time.append(jogador.copy())

    conta_partida = 0
    total_gols = 0
    gols_por_part.clear()

    opcao = input('\033[1;34mDeseja continuar? (S/N) \033[m').upper()

    if opcao == 'N':
        break

print('índice | nome | total de partidas | total gols | gols por partida')
for c, j in enumerate(time):
    print(f'{c + 1} | {j['nome']} | {j['total_partidas']} | {j['total_gols']} | {j['gols']}')

while True:
    opcao = int(input('Deseja mostrar os dados de qual jogador? (999 interrompe) '))

    if opcao == 999:
        print('Fim de programa.')
        break
    else:
        print(f'{opcao} | {time[opcao -1]['nome']} | {time[opcao -1]['total_partidas']} | {time[opcao -1]['total_gols']} | {time[opcao -1]['gols']}')

# ===== Desafio 98 =====

def area(larg, comp):
    result = larg * comp
    return result

larg = int(input('\033[1;31mDigite a largura do terreno em metros: \033[m'))
compr = int(input('\033[1;33mDigite o comprimento do terreno em metros: \033[m'))

print(f'\033[1;32mA área desse terreno é de {area(larg, compr)}m2.\033[m')

# ===== Desafio 99 =====

def mensagem(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)

msg = input('Digite a mensagem que deseja exibir: ').title()
mensagem(msg)

# ===== Desafio 100 =====

def contador(i, f, p):
    print(f'\033[1;34mContagem: Início({i}); Fim({f}); Passo({p})\033[m')
    
    if i < f:
        for n in range(i, f + 1, p):
            print(f'{n} ', end='')
    elif i > f:
        p = 0 - p
        for n in range(i, f - 1, p):
            print(f'{n} ', end='')
    print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)



