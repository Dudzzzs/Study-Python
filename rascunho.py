# ===== Desafio 14 =====

salario = float(input('Qual o salário do funcionário? '))
aumento = 15 / 100
salarioLiquido = salario + salario * aumento

print('O salário do funcionário é de {:.2F} reais e com {}% de aumento irá para {:.2f} reais.'.format(salario, aumento * 100, salarioLiquido))
