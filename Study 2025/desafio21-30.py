# ===== Desafio 21 =====

import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

print('A sequência de apresentacão é {}'.format(random.sample(alunos, k=4)))

# ===== Desafio 22 =====

import pygame

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\Dudu\Downloads\kamehameha.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

# ===== Desafio 23 =====

nome = input('Digite o seu nome completo:')

print('Nome completo em maiúsculas: {}'.format(nome.upper()))
print('Nome completo em minúsculas: {}'.format(nome.lower()))
print('Seu nome completo possui {} letras'.format(nome.replace(' ', '').__len__()))

dividido = nome.split()
print('Seu primeiro nome possui {} letras'.format(dividido[0].__len__()))

# ===== Desafio 24 =====

numero = input('Digite um número de quatro dígitos:').strip()

print('A unidade é: {}; \n A dezena é: {}; \n A centena é: {}; \n O milhar é: {};'.format(numero[3], numero[2], numero[1], numero[0]))

# ===== Desafio 25 =====

cidade = input('Digite o nome da cidade: ').strip().title()

dividido = cidade.split()
print(dividido[0])
print('A primeira palavra do nome da cidade é "Santo" ? {}'.format(dividido[0] == 'Santo'))

# ===== Desafio 26 =====

nome = str(input('Digite seu nome completo: ')).strip().title()

print('Seu nome possui "Silva" ? {}'.format('Silva' in nome))

# ===== Desafio 27 =====

frase = 'Eu amo a Deus demais'

print('A letra "a" aparece {} vezes na frase. '.format(frase.lower().count('a')))
print('A primeira posicao que a letra "a" aparece na frase é: {}'.format(frase.lower().find('a') + 1))
print('A última posicao que a letra "a" aparece na frase é: {}'.format(frase.lower().rfind('a') + 1))

# ===== Desafio 28 =====

nome = input('Digite seu nome completo:').strip().title()

dividido = nome.split()

print('O seu primeiro nome é {} e seu último nome é {}.'.format(dividido[0], dividido[len(dividido) - 1]))

# ===== Desafio 29 =====

import random

numero = random.randint(1,5)

resposta = int(input('Qual número entre 1 e 5 foi gerado pelo computador? '))

if resposta == numero:
    print('Parabéns você acertou! O número gerado foi {}'.format(numero))
else:
    print('Você errou! O número escolhido foi {}'.format(numero))

# ===== Desafio 30 =====

velocidadeCarro = int(input('Qual velocidade o carro estava?').strip())
velocidadeMax = 80

if velocidadeCarro > velocidadeMax:
    multa = (velocidadeCarro - velocidadeMax) * 7
    print('Você foi multado por ultrapassar o limite de velocidade. Você será multado em R${} por estar {}km/h acima do limite de velocidade de {}km/h.'.format(multa, velocidadeCarro - velocidadeMax, velocidadeMax ))
else:
    print('Você está dentro do limite de velocidade. Parabéns!')


