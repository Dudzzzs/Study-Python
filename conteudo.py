#Mensagens em texto
print('Olá mundo')

#Números e operações
print(6)
print(6 + 10)
print('6' + '10')

#Números + textos
print('Olá' , 5)

#Criando e usando variáveis
nome = 'Eduardo'
idade = 21
peso = 82.7

print(nome , idade , peso)

#Criando interatividade com variáveis
nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
peso = input('Qual seu peso?')

print(nome , idade , peso)

#Converter valores
int() #Transforma mensagem em números inteiros
float() #Transforma mensagem em números decimais
bool() #Transforma em booleano
str() #Transforma em string

#Format
nome = 'Eduardo'
print('Seja bem vindo {}'.format(nome)) #Substitui a chave pelo que ta escrito dentro dos parênteses

#Import
import math #Importa todo o pacote math
from math import sqrt #Importa somente a funcionalidade sqrt do pacote math
print('A raiz quadrada de {} é igual a {}'.format(81, math.sqrt(81)))

#Operadores condicionais
if 'condicao' == 'condicao': #SE a condicão for verdadeira ele executa o respectivo codigo
    'codigo'
elif 'condicao' == 'condicao': #Se a primeira condição for falsa mas ainda houver uma terceira ou outra condição (Else + If)
    'Código'
else: #SE a condicão for falsa ele executa o respectivo código
    'codigo'




