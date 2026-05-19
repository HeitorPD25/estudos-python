# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

import os
os.system('cls')

a = int(input('Valor da reta a: '))
b = int(input('Valor da reta b: '))
c = int(input('Valor da reta c: '))

if a + b > c and b + c > a and c + a > b:
    print('Podem formar um triângulo.')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não podem ser triângulos.')