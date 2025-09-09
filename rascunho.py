# ===== Desafio 67 =====

continuar = True
contaNumer = 0
soma = 0
maior = 0
menor = 0

while continuar:
    numero = int(input('Digite um número inteiro: '))

    contaNumer += 1
    soma += numero

    if menor == 0:
        menor = numero
    elif numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    

    opcao = input('\033[1;33mVocê deseja digitar mais números? (S/N)\033[m ').upper()

    if opcao == 'N':
        continuar = False
        print('\033[1;31mPrograma encerrado!\033[m')

media = soma / numero

print('Foram digitados {} números. A soma deles é {}, a média entre eles é {}, o maior foi {} e o menor {}.'.format(contaNumer, soma, media, maior, menor))


        
    