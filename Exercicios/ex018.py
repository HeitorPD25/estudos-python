# Exercício Python 018: Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import os
import math
os.system('cls')

ang = float(input('Digite o valor do seu ângulo: '))

print('Seno: ', math.sin(ang))
print('Cosseno: ', math.cos(ang))
print('Tangente: ', math.tan(ang))