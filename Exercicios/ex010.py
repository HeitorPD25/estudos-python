# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
import os
os.system('cls')

carteira = float(input('Quantos reais você possui? '))

dolares = carteira / 4.92

print(f'Você possui US${dolares:,.2f}')