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
