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

# ===== Desafio 38 =====

print('\033[1;34mOlá, Bom dia!, preciso das seguintes informações para analisarmos o empréstimo:')
valorCasa = float(input('\033[1;35mQual o valor do imóvel que deseja comprar?'))
salario = float(input('\033[1;36mQual o valor do seu salário?'))
tempo = int(input('\033[1;33mEm quantos anos deseja quitar o imóvel?'))

prestacaoMensal = valorCasa / (tempo * 12)

if prestacaoMensal > ((30/100) * salario):
    print('\033[1;31mO valor da prestação é de R${:.2f} e é maior que 30% do salário, por isso o empréstimo está NEGADO!'.format(prestacaoMensal))
else:
    print('\033[1;32mO valor da prestação de R${:.2f} é menor que 30% do seu salário e por isso seu empréstimo está APROVADO!'.format(prestacaoMensal))

# ===== Desafio 39 =====

fecharCor = '\033[m'

numero = int(input('Digite um número inteiro: '))

opcao = int(input('O número é {} digite \033[1;31m1{} para convete-lo em binário, \033[1;32m2{} para octal e \033[1;33m3{} para hexadecimal: '.format(numero, fecharCor, fecharCor, fecharCor)))

if opcao == 1:
    print('O número {} conertido em binário é: {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
     print('O número {} conertido em octal é: {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
     print('O número {} conertido em hexadecimal é: {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida')

# ===== Desafio 40 =====

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('Entre {} e {} o maior número é {}.'.format(num1, num2, num1))
elif num2 > num1:
    print('Entre {} e {} o maior número é {}.'.format(num1, num2, num2))
else:
    print('Os dois números são iguais!')


