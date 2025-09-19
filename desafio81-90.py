# ===== Desafio 81 =====

numeros = []

while True:
    n = int(input('Digite um número para ser adicionado na lista: '))

    if n in numeros:
        print('Esse número já foi adicionado.')
    else:
        numeros.append(n)

    opcao = input('Deseja continuar? (S/N) ').lower()

    if opcao == 'n':
        break

numeros.sort()
print(f'Os números adicionados em ordem crescente foram: {numeros}')

# ===== Desafio 82 =====

numeros = []

for c in range(0,4):
    n = int(input('Digite um número para ser adicionado na lista: '))
    
    posicao = 0
    if len(numeros) != 0:
        for p, num in enumerate(numeros):
            if n < numeros[p]:
                posicao = p
                break
            else:
                posicao += 1
        numeros.insert(posicao, n)
    else:
        numeros.append(n)

print(numeros)

# ===== Desafio 83 =====

numeros = []
contador = 0

while True:
    n = int(input('Digite um número para adicionar à lista: '))

    numeros.append(n)
    contador += 1

    opcao = input('Deseja continuar? (S/N) ').lower()

    if opcao == 'n':
        print('Programa finalizado!')
        break

print(f'Foram digitados {contador} números.')

decrescente = sorted(numeros, reverse=True)
print(f'A lista ordenada de forma decrescente é {decrescente}')

if 5 in numeros:
    print('O número 5 foi digitado e está incluso na lista!')
else:
    print('O número 5 não foi digitado!')

# ===== Desafio 84 =====

numeros = []
pares = []
impares = [] 

while True:
    n = int(input('Digite um número para adicionar à lista: '))

    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    opcao = input('Deseja continuar? (S/N) ').lower()

    if opcao == 'n':
        print('Programa finalizado!')
        break

print(f'\033[1;33mOs números digitados foram: {numeros}\033[m')
print(f'\033[1;32mOs pares digitados foram: {pares}\033[m')
print(f'\033[1;31mOs ímpares digitados foram: {impares}\033[m')

# ===== Desafio 85 =====

verif = []

exp = str(input('DIgite a expressão numérica: '))

for simb in exp:
    if simb == '(':
        verif.append(simb)
    elif len(verif) > 0:
        if simb == ')':
            verif.pop()
    else:
        verif.append(simb)
        break

if len(verif) > 0:
    print('\033[1;31mSua expressão está incorreta!\033[m')
else:
    print('\033[1;32mSua expressão está correta!')
   
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