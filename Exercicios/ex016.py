# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import os
import math
os.system('cls')

num = float(input('Digite um número: '))
print(math.trunc(num))