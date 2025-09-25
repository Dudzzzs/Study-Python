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





    

