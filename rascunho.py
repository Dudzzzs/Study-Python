# ===== Desafio 108 =====

def pyHelp():
    while True: 
        msg = 'Sistema de ajuda Python'
        tam = len(msg) + 4
        print('\033[7;40m=\033[m' * tam)
        print(f'\033[7;40m  {msg}  \033[m')
        print('\033[7;40m=\033[m' * tam)
        
        comando = input('Digite o comando que deseja receber aprender sobre seu funcionamento: (FIM = Encerrar) ')

        if comando == 'FIM':
            print('\033[1;31mPrograma encerrado!!\033[m')
            break
        else:
            help(comando)
           
pyHelp()