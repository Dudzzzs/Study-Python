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