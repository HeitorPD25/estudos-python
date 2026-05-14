# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
import os
os.system('cls')

nome = str(input('Digite seu Nome Completo: ')).strip()
print('silva' in nome.lower())