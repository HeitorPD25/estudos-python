# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
import os
os.system('cls')

num = int(input('Digite seu número: '))
ant = num - 1
suc = num + 1
print(f"""
      ANTECESSOR: {ant}
      NÚMERO: {num}
      SUCESSOR: {suc}
      """)
