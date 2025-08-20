algo = input('Digite algo:')

print('Algo é um número? {}'.format(algo.isnumeric()))
print('Algo são apenas letras? {}'.format(algo.isalpha()))
print('Algo são letras e/ou números? {}'.format(algo.isalnum()))
print('Algo está em letras maiúsculas? {}'.format(algo.isupper()))
print('Algo está em letras minúsculas? {}'.format(algo.islower()))