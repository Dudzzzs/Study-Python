def metade(preco, form = False):
    meio = preco / 2

    if form == True:
        meio = formatar(meio)
    
    return meio

def dobro(preco, form = False):
    dobrar = preco * 2

    if form == True:
        dobrar = formatar(dobrar)
    
    return dobrar

def aument(preco, aumento, form = False):
    aumento /= 100
    aumentar = preco + (preco * aumento)

    if form == True:
        aumentar = formatar(aumentar)
    
    return aumentar

def reduz(preco, redu, form=False):
    redu /= 100
    diminuir = preco - (preco * redu)

    if form == True:
        diminuir = formatar(diminuir)
    
    return diminuir

def formatar(preco):
    formatado = (f'{preco:.2f}'.replace('.', ','))
    return formatado

def resumo(preco, aumento, reducao):
    msg = 'RESUMO PREÇO'
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)

    print(f'\033[1;33mA metade de R${formatar(preco)} é R${metade(preco, form=True)}\033[m')
    print(f'\033[1;34mO dobro de R${formatar(preco)} é R${dobro(preco, True)}\033[m')
    print(f'\033[1;32mO preço R${formatar(preco)} acrescido de {aumento}% é R${aument(preco, aumento, form=True)}\033[m')
    print(f'\033[1;31mO preço R${formatar(preco)} reduzido de {reducao}% é R${reduz(preco, reducao, True)}\033[m')