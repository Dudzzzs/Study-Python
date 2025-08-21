# ===== Desafio 11 =====

real = float(input('Quantos reais você tem? '))
dolar = 3.27

print('Com os seus {:.2f} reais você consegue comprar {:.2f} dólares.'.format(real, real / dolar))

# ===== Desafio 12 =====

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
rendimentoTinta = 2


print('Para uma parede de {} metros de altura e {} metros de largura você irá precisar de {} litros de tinta.'.format(altura, largura, area / rendimentoTinta))

# ===== Desafio 13 =====

preco = float(input('Qual o preco do produto? '))
desconto = 5 / 100

print('O preco do produto é de {:.2f} reais e com {} % de desconto ele sairá por {:.2f} reais.'.format(preco, desconto * 100, preco - preco * desconto))

# ===== Desafio 14 =====

salario = float(input('Qual o salário do funcionário? '))
aumento = 15 / 100
salarioLiquido = salario + salario * aumento

print('O salário do funcionário é de {:.2F} reais e com {}% de aumento irá para {:.2f} reais.'.format(salario, aumento * 100, salarioLiquido))

