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

#Loop FOR
for c in range('x, y, z'): #C é o index de referencia. Range é o intervalo de vezes que o comando irá ser executado, sendo que é sempre uma vez menos que o último número. Z é o salto de contagem.
    'código'

#Loop WHILE
while 'condição': #While significa “ENQUANTO”, ou seja, enqaunto a condição estabelecida for suprida ele executará o código.
    'código'

#Variáveis compostas: São variáveis que podem armazenar mais de um valor
#Tuplas: São varáveis que não podem ser aletaradas seus valores durante a execução do  código
tuplas = ('valor', 'valor', 'valor')

#As listas diferentes das tuplas são mutáveis, o que permite adicionar, remover e mudar valores das listas
listas = ['valor', 'valor', 'valor']

listas.append() #Adiciona elementos no fim da lista

listas.insert(0, 'valor') #Adiciona o valor na posição 0 e arras os outros elementos para frente, o 0 vira o 1 por exemplo

del listas[3] #Exlui o elemento que estava na posição 3

listas.pop(3) #O método pop exclui o último elemento da lista mas posso indicar o índice que quero excluir

listas.remove('valor') #Exclui o valor escolhido da lista

#Quando excluímos valores das listas os índices são resposicionados para trás, excluindo o 3 o item 4 vira o 3 por exemplo.

listas.sort() #Ordena os elementos da lista em ordem crescente