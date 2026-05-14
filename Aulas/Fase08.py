# Utilizando módulos
# Para importar uma biblioteca use 'import {biblioteca}'
# Se quiser importar apenas um método use 'from {biblioteca} import {método}'

import math
# ceil -> arredonda pra cima 
print(math.ceil(10.25))
# floor -> arredonda para baixo
print(math.floor(10.25))
# trunc -> não exibe as decimais
print(math.trunc(10.25))
# pow -> potência
print(math.pow(2, 5))
# sqrt -> raíz quadrada
print(math.sqrt(25))
# factorial -> calcula o fatorial
print(math.factorial(5))
# E vários outros métodos

import random
# random gera um número aleatório entre 0 e 1
print(random.random())
# randint gera um inteiro aleatório no intervalo que eu determinar
print(random.randint(1, 10))

import emoji
print(emoji.emojize("Testantando emojis :💩"))
