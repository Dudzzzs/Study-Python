# ===== Desafio 91 =====

aluno = []
sala = []

while True:
    aluno.clear()

    nome = input('Digite o nome do aluno: ').title()
    aluno.append(nome)
    nota1 = float(input('Digite a nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Digite a nota 2: '))
    aluno.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(media)

    sala.append(aluno[:])

    opcao = input('Deseja continuar? [S/N] ').upper()

    if opcao == 'N':
        break

print(f'\033[1;33mAluno | Nome | Nota 1 | Nota 2 | Média\033[m')
print('-=' * 20)

for c in range(0, len(sala)):
    print(f'{c + 1:^5} | {sala[c][0]:^5} | {sala[c][1]:^5} | {sala[c][2]:^5} | {sala[c][3]:^5}')

while True:
    a = int(input('Deseja mostrar a nota de qual aluno? (0 interrompe) '))

    if a == 0:
        break
    elif a - 1 > len(sala):
        print('Esse aluno não existe!')
    else:
        print(f'{a:^5} | {sala[a - 1][0]:^5} | {sala[a - 1][1]:^5} | {sala[a - 1][2]:^5} | {sala[a - 1][3]:^5}')

    if a == 0:
        break
        
print('\033[1;31mPrograma finalizado!\033[m')