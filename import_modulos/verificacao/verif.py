def verificacao(preco):

    if preco.isalpha() or preco ==  '':
        print('\033[1;31mERRO! DIGITE UM PREÇO VÁLIDO!!\033[m')
        return False
    else:
        return True





