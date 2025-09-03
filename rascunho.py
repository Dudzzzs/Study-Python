# ===== Desafio 44 =====

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
triangulo = str

if r1 == r2 and r2 == r3:
    triangulo = 'equilátero'
elif r1 == r2 or r2 == r3 or r1 == r3:
    triangulo = 'isósceles'
elif r1 != r2 and r1 != r3 and r2 != r3:
    triangulo = 'escaleno'


if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Com essas 3 retas de comprimento {}, {} e {} você pode formar um triângulo {}!'.format(r1, r2, r3, triangulo))
else:
    print('Com essas 3 retas de comprimento {}, {} e {} você não pode formar um triângulo!'.format(r1, r2, r3))
