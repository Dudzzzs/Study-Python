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