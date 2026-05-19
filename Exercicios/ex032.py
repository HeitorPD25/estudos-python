# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import os
os.system('cls')

ano = int(input('Digite seu ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é bissexto.')
else:
    print(f'O Ano {ano} não é bissexto.')