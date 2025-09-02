# ===== Desafio 31 =====

numero = int(input('Digite um número inteiro: ').strip())

if numero % 2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))

# ===== Desafio 32 =====

distancia = int(input('Qual a distância em km da viagem?').strip())

if distancia <= 200:
    preco = 0.5 * distancia
    print('Para uma viagem de {} quilômetros o preco da passagem é R${:.2f}'.format(distancia, preco))
else:
    preco = 0.45 * distancia
    print('Para uma viagem de {} quilômetros o preco da passagem é R${:.2f}'.format(distancia, preco))

# ===== Desafio 33 =====

ano = int(input('Digite um ano: ').strip())

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))

# ===== Desafio 34 =====

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
numMaior = 0
numMenor = 0

#Verificando maior
if num1 > num2 and num1 > num3:
    numMaior = num1
elif num2 > num1 and num2 > num3:
    numMaior = num2
else:
    numMaior = num3

#Verificando menor
if num1 < num2 and num1 < num3:
    numMenor = num1
elif num2 < num1 and num2 < num3:
    numMenor = num2
else:
    numMenor = num3
    
print('O maior número entre {}, {} e {} é {} e o menor é {}.'.format(num1, num2, num3, numMaior, numMenor))

# ===== Desafio 35 =====

salario = float(input('Digite o seu salário: '))

if salario <= 1250:
    percentual = 15 / 100
    aumento = salario + (salario * percentual)
    print('O salário de R${:.2f} irá aumentar {}% e irá para R${:.2f}'.format(salario, percentual * 100, aumento))
else:
    percentual = 10 / 100
    aumento = salario + (salario * percentual)
    print('O salário de R${:.2f} irá aumentar {}% e irá para R${:.2f}'.format(salario, percentual * 100, aumento))

# ===== Desafio 36 =====

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Com essas 3 retas de comprimento {}, {} e {} você pode formar um triângulo!'.format(r1, r2, r3))
else:
    print('Com essas 3 retas de comprimento {}, {} e {} você não pode formar um triângulo!'.format(r1, r2, r3))

# ===== Desafio 37 =====

numeroI = int(input('Digite o número inicial da contagem:').strip())
numeroF = int(input('Digite o número final da contagem:').strip())

if numeroI < numeroF:
    while numeroI <= numeroF:
        print('\033[1;32m{}\033[m'.format(numeroI))
        numeroI = numeroI + 1
else:
    while numeroI >= numeroF:
        print('\033[1;31m{}\033[m'.format(numeroI))
        numeroI = numeroI - 1

