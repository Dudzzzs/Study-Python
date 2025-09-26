# ===== Desafio 102 =====

import random

def contador(*num):
    maior = 0

    for n in num:
        if n > maior:
            maior = n

    print(f'\033[1;32mO maior número entre {num} é {maior}: \033[m')

contador(1, 2, 43)





    

