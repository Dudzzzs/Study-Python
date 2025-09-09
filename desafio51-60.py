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

# ===== Desafio 55 =====

frase = input('Digite uma frase para verificar se é ou não um palíndromo: ').strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''

for letras in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letras]

if inverso == juntas:
    print('A frase {} \033[1;33mé um palíndromo!\033[m'.format(frase))
else:
    print('A frase {} \033[1;31mnão é um palíndromo!\033[m'.format(frase))

# ===== Desafio 56 =====

nomes = []
idade = []
contador = 0
contadorVerif = 0

for c in range(1, 8):
    nome = input('Digite seu nome: ').title()
    anoNasc = int(input('Qual seu ano de nascimento? '))
    print('Cadastro realizado!')
    nomes.insert(contador, nome)
    idade.insert(contador, 2025 - anoNasc)
    contador += 1

for c in range(1, len(nomes) + 1):
    if idade[contadorVerif] >= 18:
        print('\033[1;33mParabéns {}, você já atingiu a maioridade pois tem {} anos.\033[m'.format(nomes[contadorVerif], idade[contadorVerif]))
    else:
        print('\033[1;31mVocê {} ainda não atingiu a maioridade pois tem {} anos.\033[m'.format(nomes[contadorVerif], idade[contadorVerif]))
    contadorVerif += 1

# ===== Desafio 57 =====

maiorPeso = 0
maisPesado = ''
menorPeso = 0
maisLeve = ''

for c in range(1, 6):
    nome = input('Digite seu nome: ').title()
    peso = float(input('Digite seu peso em quilos: '))
    print('CADASTRO REALIZADO!')
    if peso > maiorPeso:
        maiorPeso = peso
        maisPesado = nome
    if c == 1:
        menorPeso = peso
        maisLeve = nome
    elif peso < menorPeso:
        menorPeso = peso
        maisLeve = nome

print('O mais pesado é o \033[1;31m{} pesando {:.1f} quilos\033[m. E o mais leve é o \033[1;32m{} pesando {:.1f} quilos\033[m.'.format(maisPesado, maiorPeso, maisLeve, menorPeso))

# ===== Desafio 58 =====

idadeMaior = 0
maisVelho = ''
somaidades = 0
mulherMenor20 = 0

for c in range(1, 6):
    nome = input('Qual seu nome? ').title()
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo? ')
    print('CADASTRO REALIZADO!')

    somaidades += idade

    if sexo == 'masculino':
        if idade > idadeMaior:
            idadeMaior = idade
            maisVelho = nome
    elif sexo == 'feminino':
        if idade < 20:
            mulherMenor20 += 1

mediaIdades = somaidades / 5

print('A média de idade dessas pessoas é {} anos, o homem mais velho é o {} com {} anos e {} mulheres possuem menos de 20 anos.'.format(mediaIdades, maisVelho, idadeMaior, mulherMenor20))

# ===== Desafio 59 =====

sexo = input('Qual seu sexo? (M/F) ').upper()
  
while sexo != 'M' and sexo != 'F':
    print('Você digitou algo que não é o seu sexo!')
    sexo = input('Qual o seu sexo? (M/F) ').upper()

if sexo == 'M':
    print('Você é homem!')
elif sexo == 'F':
    print('Você é mulher!')

print('FIM')

# ===== Desafio 60 =====

import random

numero = random.randint(1,10)
palpites = 1

resposta = int(input('Qual número entre 1 e 10 foi gerado pelo computador? '))

while numero != resposta:
    print('Você errou!')
    resposta = int(input('Qual número entre 1 e 10 foi gerado pelo computador? '))
    palpites+=1

print('Parabéns você acertou! O número gerado foi {}. Foram necessários {} palpites.'.format(numero, palpites))
