# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
import os
os.system('cls')

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O maior número é {maior}')