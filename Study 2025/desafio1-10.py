# ===== Desafio 1 =====
nome = input('Qual seu nome?')

print('Olá, seja bem vindo ' + nome)

# ===== Desafio 2 =====

dia = input('Qual seu dia de nascimento?')
mes = input('Qual seu mês de nascimento?')
ano = input('Qual seu ano de nascimento?')

print('Você nasceu dia ' , dia , ' de ' , mes , ' de ' , ano , '. Correto?')

# ===== Desafio 3 =====

primeironum = int(input('Qual o primeiro número?'))
segundonum = int(input('Qual o segundo número?'))
soma = primeironum + segundonum

print('A soma é: ' , soma)

# ===== Desafio 4 =====

num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))
soma = num1 + num2

print('A soma entre {} e {} é {}'.format(num1, num2, soma))

# ===== Desafio 5 =====

algo = input('Digite algo:')

print('Algo é um número? {}'.format(algo.isnumeric()))
print('Algo são apenas letras? {}'.format(algo.isalpha()))
print('Algo são letras e/ou números? {}'.format(algo.isalnum()))
print('Algo está em letras maiúsculas? {}'.format(algo.isupper()))
print('Algo está em letras minúsculas? {}'.format(algo.islower()))

# ===== Desafio 6 =====

numero = int(input('Digite um número:'))

print('O sucessor de {} é {} e o seu antecessor é {}.'.format(numero, numero + 1, numero - 1))

# ===== Desafio 7 =====

numero = int(input('Digite um número:'))

print('O dobro de {} é {}, o triplo é {} e raiz quadrada é {}.'.format(numero, numero * 2, numero * 3, numero ** (1/2)))

# ===== Desafio 8 =====

nome = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a primeira nota do aluno: '))
nota2 = int(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print('Olá {}, sua primeira nota foi {} e sua segaunda nota foi {}, portanto a sua média é de {:.1f} pontos.'.format(nome, nota1, nota2, media))
# ===== Desafio 9 =====

valor = float(input('Quantos metros tem a mesa? '))

print('Então sua mesa de {} metros tem {} centimetros e {} milimetros.'.format(valor, valor * 100, valor * 1000))

# ===== Desafio 10 =====

numero = float(input('Digite um número para calcular sua tabuada: '))

print('Tabuada do {:.2F}: '.format(numero))
print('{:.2F} x 1 = {:.2F}'.format(numero, numero * 1))
print('{:.2F} x 2 = {:.2F}'.format(numero, numero * 2))
print('{:.2F} x 3 = {:.2F}'.format(numero, numero * 3))
print('{:.2F} x 4 = {:.2F}'.format(numero, numero * 4))
print('{:.2F} x 5 = {:.2F}'.format(numero, numero * 5))
print('{:.2F} x 6 = {:.2F}'.format(numero, numero * 6))
print('{:.2F} x 7 = {:.2F}'.format(numero, numero * 7))
print('{:.2F} x 8 = {:.2F}'.format(numero, numero * 8))
print('{:.2F} x 9 = {:.2F}'.format(numero, numero * 9))
print('{:.2F} x 10 = {:.2F}'.format(numero, numero * 10))