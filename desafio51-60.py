# ===== Desafio 51 =====

numero = int(input('Qual número você deseja saber a tabuada? '))
contador = 1

for c in range(1, 11, 1):
    resultado = numero * contador
    print('{} x {} = {}'.format(numero, contador, resultado))
    contador = contador + 1

# ===== Desafio 52 =====

somasPares = 0
pares = []

for c in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        pares.append(numero)
        somasPares = somasPares + numero
print('A soma dos números pares que você digitou ({}) é: {}'.format(pares, somasPares))

# ===== Desafio 53 =====

primeiroTermo = int(input('Qual o primeiro termo da progressão da progressão aritmética? '))
razao = int(input('Qual é a razão da progressão da progressão aritmética? '))
decimoTermo = primeiroTermo + (10 - 1) * razao

print('Os 10 primeiros termos da sua PA de primeiro termo {} e razão {} são:'.format(primeiroTermo, razao))

for c in range(primeiroTermo, decimoTermo + 1, razao):
    print(c)   

# ===== Desafio 54 =====

for c in range(1, 6):
    numero = int(input('Digite um número inteiro: '))
    divisiveis = []
    for n in range(1, numero + 1, 1):
        if numero % n == 0:
            divisiveis.append(n)
    if len(divisiveis) == 2:
        print('O número {} \033[1;32mÉ PRIMO!\033[m'.format(numero))
    else:
        print('O número {} \033[1;31mNÃO É PRIMO!\033[m'.format(numero)) 