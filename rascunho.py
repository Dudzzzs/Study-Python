# ===== Desafio 58 =====

idadeMaior = 0
maisVelho = ''
somaidades = 0
mulherMenor20 = 0

for c in range(1, 6):
    nome = input('Qual seu nome? ').title()
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo? ')
    print('CADASTRO REALIZADO!')

    somaidades += idade

    if sexo == 'masculino':
        if idade > idadeMaior:
            idadeMaior = idade
            maisVelho = nome
    elif sexo == 'feminino':
        if idade < 20:
            mulherMenor20 += 1

mediaIdades = somaidades / 5

print('A média de idade dessas pessoas é {} anos, o homem mais velho é o {} com {} anos e {} mulheres possuem menos de 20 anos.'.format(mediaIdades, maisVelho, idadeMaior, mulherMenor20))