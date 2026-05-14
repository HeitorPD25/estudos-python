#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import os
import math
os.system('cls')

cateto_adj = float(input('Digite o valor do cateto adjacente: '))
cateto_opo = float(input('Digite o valor do cateto oposto: '))

hipotenusa = math.sqrt(math.pow(cateto_adj, 2) + math.pow(cateto_opo, 2))

print(f'Sua fórmula ficou a² = {cateto_opo}² + {cateto_adj}², sendo a = {hipotenusa:,.2f}')
