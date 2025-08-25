# ===== Desafio 22 =====

import pygame

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\Dudu\Downloads\kamehameha.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue




