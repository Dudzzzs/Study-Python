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

maisTermos = True

while maisTermos:
    opcao = int(input('Quantos termos você deseja saber a mais? '))

    if opcao == 0:
        maisTermos = False
        print('\033[1;31mPrograma finalizado!\033[m')
    else:
        for c in range(contaTermo, contaTermo + opcao): 
            termo += razao
            print('{}º termo: {}'.format(contaTermo, termo))

            contaTermo +=1

# ===== Desafio 65 =====

quantiTermos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
contaTermos = 1

while contaTermos <= quantiTermos:
    if contaTermos == 1:
        print('{}º termo: {}'.format(contaTermos, t1))
        print('2º termo: {}'.format(t2))
        contaTermos = 3
    else:
        t3 = t1 + t2
        print('{}º termo: {}'.format(contaTermos, t3) )
        t1 = t2
        t2 = t3

    contaTermos += 1

# ===== Desafio 66 =====

continuar = True
quantidadeNumeros = 0
soma = 0

while continuar:
    numero = int(input('Digite um número: '))

    if numero == 999:
        print('\033[1;31mCondição de parada atingida. Programa encerrado!\033[m')
        continuar = False
    else:
        quantidadeNumeros += 1
        soma += numero

print('Foram digitados {} números antes da condição de parada, e a soma entre eles é {}'.format(quantidadeNumeros, soma))

# ===== Desafio 67 =====

continuar = True
contaNumer = 0
soma = 0
maior = 0
menor = 0

while continuar:
    numero = int(input('Digite um número inteiro: '))

    contaNumer += 1
    soma += numero

    if menor == 0:
        menor = numero
    elif numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    

    opcao = input('\033[1;33mVocê deseja digitar mais números? (S/N)\033[m ').upper()

    if opcao == 'N':
        continuar = False
        print('\033[1;31mPrograma encerrado!\033[m')

media = soma / numero

print('Foram digitados {} números. A soma deles é {}, a média entre eles é {}, o maior foi {} e o menor {}.'.format(contaNumer, soma, media, maior, menor))
    