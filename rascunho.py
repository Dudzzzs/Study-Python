# ===== Desafio 86 =====

pessoas = []
nome_peso = []
pesadas = []
leves = []
contador = 0

while True:
    n = input('Digite o nome da pessoa: ').title()
    p = int(input('Digite o peso dessa pessoa: '))

    nome_peso.append(n)
    nome_peso.append(p)
    pessoas.append(nome_peso[:])
    contador += 1
    
    if len(pesadas) == 0:
        pesadas.append(nome_peso[:])
    elif nome_peso[1] > pesadas[0][1]:
        pesadas.clear()
        pesadas.append(nome_peso[:])
    elif nome_peso[1] == pesadas[0][1]:
        pesadas.append(nome_peso[:])

    if len(leves) == 0:
        leves.append(nome_peso[:])
    elif nome_peso[1] < leves[0][1]:
        leves.clear()
        leves.append(nome_peso[:])
    elif nome_peso[1] == leves[0][1]:
        leves.append(nome_peso[:])

    nome_peso.clear()

    opcao = input('Deseja continuar? (S/N) ').lower()

    if opcao == 'n':
        print('Programa finalizado!')
        break

print(f'Foram cadastradas {contador} pessoas')

texto_pesado = f'O maior peso foi de {pesadas[0][1]}kg. Peso de '
for i, nome in enumerate(pesadas):
    texto_pesado += f'[{pesadas[i][0]}] '

print(texto_pesado)

texto_leve = f'O menor peso foi de {leves[0][1]}kg. Peso de '
for i, nome in enumerate(leves):
    texto_leve += f'[{leves[i][0]}] '

print(texto_leve)    