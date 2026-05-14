# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import os
os.system('cls')

num = int(input('Digite seu número: '))

dobro = num * 2
triplo = num * 3
raiz = num ** 0.5

print(f'''
      Seu número: {num}
      Dobro: {dobro}
      Triplo: {triplo}
      Raiz Quadrada: {raiz}
      ''')
