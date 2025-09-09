# ===== Desafio 61 =====

continuar = True

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while continuar:

    print('O que você deseja fazer com os números {} e {}? \n1: Somar; \n2: Multiplicar; \n3: Maior; \n4: Novos números; \n5: Sair do programa.'.format(num1, num2))
    opcao = int(input(''))

    if opcao == 1:
        soma = num1 + num2
        print('A soma de {} e {} é {}.'.format(num1, num2, soma))

    if opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicação de {} por {} é {}.'.format(num1, num2, multiplicacao))

    if opcao == 3:
        maior = 0
        if num1 > num2:
            maior = num1
            print('Entre {} e {} o maior número é {}.'.format(num1, num2, maior))
        elif num2 > num1:
            maior = num2
            print('Entre {} e {} o maior número é {}.'.format(num1, num2, maior))
        else:
            print('Os números são iguais.')
    
    if opcao == 4:
        num1 = int(input('Digite um novo primeiro número: '))
        num2 = int(input('Digite um novo segundo número: '))
        print('Números atualizados!')
    
    if opcao == 5:
        continuar = False
        print('\033[1;31mPrograma finalizado!\033[m')

    if opcao != 5:
        fluxo = input('\033[1;33mDeseja continuar? (S/N)\033[m ').upper()

        if fluxo == 'N':
            continuar = False
            print('\033[1;31mPrograma finalizado!\033[m')

# ===== Desafio 62 =====

from math import factorial

continuar = True

while continuar:
    numero = int(input('Digite um número para descobrir o seu fatorial: '))
    fatorial = factorial(numero)

    print('O fatorial de {} é {}.'.format(numero, fatorial))

    fluxo = input('\033[1;33mDeseja continuar? (S/N)\033[m ').upper()

    if fluxo == 'N':
            continuar = False
            print('\033[1;31mPrograma finalizado!\033[m')

# ===== Desafio 63 =====

primeiroTermo = int(input('Qual o primeiro termo da progressão da progressão aritmética? '))
razao = int(input('Qual é a razão da progressão da progressão aritmética? '))

print('Os 10 primeiros termos da sua PA de primeiro termo {} e razão {} são:'.format(primeiroTermo, razao))

contaTermo = 1
termo = 0

while contaTermo <= 10:
    
    if contaTermo == 1:
        termo = primeiroTermo
        print('{}º termo: {}'.format(contaTermo, termo))
    else:
        termo += razao
        print('{}º termo: {}'.format(contaTermo, termo))
    
    contaTermo += 1

# ===== Desafio 64 =====

primeiroTermo = int(input('Qual o primeiro termo da progressão da progressão aritmética? '))
razao = int(input('Qual é a razão da progressão da progressão aritmética? '))

print('Os 10 primeiros termos da sua PA de primeiro termo {} e razão {} são:'.format(primeiroTermo, razao))

contaTermo = 1
termo = 0

while contaTermo <= 10:
    if contaTermo == 1:
        termo = primeiroTermo
        print('{}º termo: {}'.format(contaTermo, termo))
    else:
        termo += razao
        print('{}º termo: {}'.format(contaTermo, termo))

    contaTermo += 1
    
opcao = int(input('Quantos termos você deseja saber a mais? '))

if opcao == 0:
    print('\033[1;31mPrograma finalizado!\033[m')
else:
    for c in range(contaTermo, contaTermo + opcao): 
        termo += razao
        print('{}º termo: {}'.format(contaTermo, termo))

        contaTermo +=1

if opcao != 0:
    print('\033[1;31mPrograma finalizado!\033[m')

