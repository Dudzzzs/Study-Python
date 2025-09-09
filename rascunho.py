# ===== Desafio 63 =====

primeiroTermo = int(input('Qual o primeiro termo da progressão da progressão aritmética? '))
razao = int(input('Qual é a razão da progressão da progressão aritmética? '))

print('Os 10 primeiros termos da sua PA de primeiro termo {} e razão {} são:'.format(primeiroTermo, razao))

contaTermo = 1
termo = 0

while contaTermo <= 10:
    if contaTermo == 1:
        termo = primeiroTermo
        print('{}º termo: {}'.format(contaTermo, termo))
    else:
        termo += razao
        print('{}º termo: {}'.format(contaTermo, termo))

    contaTermo += 1
    
opcao = int(input('Quantos termos você deseja saber a mais? '))

if opcao == 0:
    print('\033[1;31mPrograma finalizado!\033[m')
else:
    for c in range(contaTermo, contaTermo + opcao): 
        termo += razao
        print('{}º termo: {}'.format(contaTermo, termo))

        contaTermo +=1

if opcao != 0:
    print('\033[1;31mPrograma finalizado!\033[m')

        
    




        
    