pessoa = {}
galera = []

def banco_dados(opcao):

    if opcao == 1:
        pessoa['nome'] = input('Qual o nome da pessoa? ').title()
        pessoa['idade'] = int(input('Quantos anos ela tem? '))

        galera.append(pessoa.copy())

        print('\033[1;32mPessoa cadastrada com sucesso!\033[m')
    
    if opcao == 2:
        if len(galera) == 0:
            print('\033[1;31mNenhuma pessoa foi adicionada!\033[m')
        else:
            msg = '\033[1;33mPESSOAS\033[m'
            tam = len(msg) + 4
            print('=' * tam)
            print(f'       {msg}')
            print()
            for p in galera:
                print(f'\033[1;36m{p['nome']} com {p['idade']} anos\033[m')
            print()
