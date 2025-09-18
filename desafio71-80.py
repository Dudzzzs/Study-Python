# ===== Desafio 71 =====

maiorDezoito = 0
homens = 0
mulherMenorD20 = 0

while True:
    input('Como chama a pessoa que quer cadastrar? ')
    idade = int(input('Quantos ela tem? '))
    sexo = input('Qual o sexo dela? (M/F) ').upper()

    if idade > 18:
        maiorDezoito += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulherMenorD20 += 1
    
    opcao = input('Deseja continuar? (S/N) ').upper()

    if opcao == 'N':
        break

print(f'Foram cadastradas {maiorDezoito} pessoas com mais de 18 anos. Foram cadastrados {homens} homens no total e {mulherMenorD20} mulheres com menos de 20 anos')

# ===== Desafio 72 =====

totalProdutos = 0
totalPreco = 0
maiorQ1000 = 0
precoMaisBarato = 0
produtoMaisBarato = ''

while True:
    nome = input('Digite o nome do produto que deseja adicionar no pedido: ')
    preco = float(input('Qual o preço dele? '))

    totalPreco += preco
    totalProdutos += 1

    if precoMaisBarato == 0:
        precoMaisBarato = preco
        produtoMaisBarato = nome
    elif preco < precoMaisBarato:
        precoMaisBarato = preco
        produtoMaisBarato = nome
    
    if preco > 1000:
        maiorQ1000 += 1
    
    opcao = input('Deseja adicionar mais algum produto? (S/N) ').upper()

    if opcao == 'N':
        print('\033[1;32mCompra finalizada\033[m')
        break

print(f'Foram adicionados {totalProdutos} produtos totalizando R${totalPreco:.2f}, sendo {maiorQ1000} produtos custando mais de 1000 reais. O produto mais barato adicionado foi {produtoMaisBarato} custando R${precoMaisBarato}.')

# ===== Desafio 73 =====

totNota = 0
notaAtu = 50

valor = int(input('Digite um valor inteiro que deseja sacar: R$'))

while True:
   if valor >= notaAtu:
      valor -= notaAtu
      totNota += 1
   else:
        print(f'{totNota} notas de R${notaAtu}.')
        if notaAtu == 50:
            notaAtu = 20
        elif notaAtu == 20:
            notaAtu = 10
        elif notaAtu == 10:
            notaAtu = 1
        totNota = 0    
        if valor == 0:
            print('Saque realizado!')
            break

# ===== Desafio 74 =====

numerosExtensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numeroInt = int(input('Digite um número inteiro de 0 a 20: '))

if numeroInt < 0 or numeroInt > 10:
    while True:
        numeroInt = int(input(' Tente novamente! Digite um número inteiro de 0 a 20: '))
        if numeroInt >= 0 and numeroInt <= 20:
            break

print(f'O número escolhido foi {numerosExtensos[numeroInt]}.')

# ===== Desafio 75 =====

times_brasileirao = ("Flamengo", "Cruzeiro", "Palmeiras", "Mirassol", "Bahia", "Botafogo", "São Paulo", "Red Bull Bragantino", "Corinthians", "Fluminense", "Ceara","Internacional", "Atletico-MG", "Gremio", "Vasco da Gama", "Santos", "Vitoria", "Juventude", "Fortaleza", "Sport")

while True:
    print('\033[1;33mO que você deseja saber sobre a tabela do brasileirão séria A 2025? \n1: Saber os 5 primeiros colocados; \n2: Saber os últimos 4 colocados; \n3: Uma lista com os times em ordem alfabética; \n4: Em que posição está o seu time; \n5: Finalizar programa.\033[m')
    opcao = int(input('Digite sua opção: '))

    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('\033[1;31mOpção inválida\033[m')

    if opcao == 1:
        top5 = []
        for posicao, time in enumerate(times_brasileirao[:5]): 
            top5.append(f'{posicao + 1}º colocado: {time}')
        top5 = ', '.join(top5)
        print (f'\033[1;32mOs 5 primeiros colocados são: {top5}.\033[m')
    
    if opcao == 2:
        z4 = []
        for posicao, time in enumerate(times_brasileirao[::-1][:4]):
            z4.append(f'{len(times_brasileirao) - posicao }º colocado: {time}')
        z4 = ', '.join(z4)
        print(f'\033[1;31mOs últimos colocados são: {z4}.\033[m')

    if opcao == 3:
        ordem_alfabetica = sorted(times_brasileirao)
        ordem_alfabetica = ', '.join(ordem_alfabetica)
        print(f'\033[1;35mOs times organizados em ordem alfabética ficam asssim: {ordem_alfabetica}.\033[m')
    
    if opcao == 4:
        time = input('Qual o seu time? ').title()
        print(f'\033[1;36mO seu time é o {time} e é o {times_brasileirao.index(time) + 1}º colocado.\033[m')

    if opcao == 5:
        print('\033[1;31mPrograma finalizado!\033[m')       
        break

# ===== Desafio 76 =====

import random

numeros = (random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000))
em_ordem = sorted(numeros)

menor = em_ordem[0]
maior = em_ordem[-1]

print(f'Os números gerados foram {numeros}. O maior é {maior} e o menor é {menor}.')

# ===== Desafio 77 =====

import random

numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(f'\033[1;32mOs números gerados foram {numeros}\033[m')

print(f'\033[1;33mO nmúmero 9 foi gerado {numeros.count(9)} vezes\033[m')

if 3 in numeros:
    print(f'\033[1;34mA primeira posição que o valor 3 foi gerado foi na {numeros.index(3) + 1}º posição.\033[m')
else:
    print('\033[1;31mO número 3 não foi gerado nenhuma vez!\033[m')

print(f'\033[1;35mOs números pares gerados foram: {pares}.\033[m')

# ===== Desafio 78 =====

tintas = ('Rende muito', 355, 'Toque fosco', 500, 'Toque fosco completo', 661, 'Toque seda', 730, 'Toque brilho', 790, 'Sempre limpo', 850)

for i in range(0, len(tintas), 2):
    print(f'{tintas[i]} {8 * '.'} R${tintas[i + 1]:.2f}') 
    
# ===== Desafio 79 =====

palavras = ('Eduardo', 'Lucas', 'Ana', 'Alice', 'Ariane')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end= ' ')

# ===== Desafio 80 =====

numeros = []
maior = 0
menor = 0

for c in range(1, 6):
    n = int(input('Digite um valor para ser adicionado na lista: '))
    numeros.append(n)

    if menor == 0:
        menor = n
    elif n < menor:
        menor = n
    if n > maior:
        maior = n

copia = numeros[:]
copia = ', '.join(map(str, numeros))

print(f'Os números digitados foram {copia}, sendo {maior} o maior estando na posição ', end='')
for i, num in enumerate(numeros):
    if num == maior:
        print(f'{i}, ', end='')
print(f'e o menor sendo {menor} estando na posição ')
for i, num in enumerate(numeros):
    if num == menor:
        print(f'{i}, ', end='')



    


