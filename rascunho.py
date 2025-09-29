# ===== Desafio 106 =====

def leiaInt(resp):
    
    ok = False
    valor = 0

    while ok == False:
        n = str(input(resp))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else: 
            print('\033[1;31mERRO, DIGITE UM NÚMERO!\033[m')
    
    return valor

n = leiaInt('Digite um número: ')
print(f'\033[1;32mVOCÊ DIGITOU O NÚMERO {n}')