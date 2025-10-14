# ===== Desafio 117 =====

from import_modulos.pessoas import pessoas

while True:
    msg = '\033[1;33mMENU PRINCIPAL \033[m'
    tam = len(msg) + 4
    print('=' * tam)
    print(f'       {msg}')
    print()
    print('\033[1;35m1: Cadastrar pessoa; \n2: Exibir pessoas; \n3: Sair do programa.\033[m')
    print('=' * tam)

    opcao = int(input('\033[1;35mOpção: \033[m'))

    if opcao == 3:
        print('\033[1;34mPrograma encerrado!\033[m')
        break
    else:
        pessoas.banco_dados(opcao)
    
   
