# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
import os
os.system('cls')

pt = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

for c in range(pt, pt+10*razao, razao):
    print(f'''{c} -> ''', end=' ')
print('Acabou')