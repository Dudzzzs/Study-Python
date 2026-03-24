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

listas.sort(reverse=True) #Ordena de forma decrescente

#Os dicionários armazenam dados literais, com eles posso não apenas guardar, mas também posso identificar os dados.
dicionarios = {'nome': 'eduardo', 'idade': 21}

dicionarios['sexo'] = 'masculino' #Adiciona dados ao dicionário

del dicionarios["idade"] #Exclui o dado “idade”

dicionarios.values() #Pega os valores do dicionário, nesse caso: Eduardo e 21

dicionarios.keys() #Pega as “chaves” ou identificadores dos dicionários, nesse caso: Nome e idade

dicionarios.items() #Pegas as chaves e os valores do dicionário, nesse caso: Nome: Eduardo e idade: 21

dicionarios.copy() #Cria uma cópia do dicionário que me permite adicioná-lo em uma lista sem criar relação indesejada

def funcao(): #Cria uma função que executa um código determinado recebendo os parâmetros que eu escolho
    'codigo'

def funcao(a, b, c=0): #Cria uma função onde o parâmetro C é opcional, podendo declará-lo ou não.
    'codigo'
    return 'valor' #Faz com que a função não apenas execute um código mas tambem retorna um valor que posso usar

#Para manter o meu código mais organizado eu posso “modularizar” algumas funções, isso seria colocar ela em outro arquivo separado do programa principal. Nesse arquivo separado posso guardar funções úteis a mim e exportar ela para outros programas.

import math #Consigo importar do arquivo "math" todas as funções presentes nele.

from math import factorial #Importo apenas a função factorial do arquivo math

math.factorial() #Uso a função factorial do arquivo math

#Tratamento de erro e exceções. Erros acontecem no python quando há um erro de sintaxe ou semântica no código.

try: #O python tenta executar o código para saber se dá erro
    'código'

except: #Caso haja erro o python executa o código seguinte
    'codigo'

#except TypeError: O python executa o seguinte código caso o erro seja de tipo de dado
    'codigo'

#except Exception as erro: Cria a varável erro que posso usar para exibir a informação que quero do erro, como `erro.__class__` que exibe a classe do erro
    'codigo'

else: #Caso não haja erro pyton executa o seguinte código
    'codigo'

finally: #O python executa o código independente de haver erro ou não
    'codigo'