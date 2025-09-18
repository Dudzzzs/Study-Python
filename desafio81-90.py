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
