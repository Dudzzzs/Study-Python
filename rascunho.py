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