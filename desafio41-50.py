# ===== Desafio 41 =====

nasc = int(input('Qual seu ano de nascimento? '))
idade = 2025 - nasc

if idade < 18:
    tempo = 18 - idade
    print('Faltam {} anos para você se alistar.'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Já se passaram {} anos do seu tempo de alistamento.'.format(tempo))
else:
    print('Está na sua época de alistamento.')

# ===== Desafio 42 =====

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi de {:.1F} e por isso você foi REPROVADO.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi de {:.1F} e por isso você está de RECUPERAÇÃO.'.format(media))
else:
    print('Sua média foi de {:.1F} e por isso você foi APROVADO.'.format(media))

# ===== Desafio 43 =====

nasc = int(input('Qual seu ano de nascimento? '))
idade = 2025 - nasc

if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade > 15 and idade <= 19:
    print('Você tem {} anos e sua categoria é JÚNIOR.'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER.'.format(idade))

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
