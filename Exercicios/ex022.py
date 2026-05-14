# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#       - O nome com todas as letras maiúsculas e minúsculas.
#       - Quantas letras ao todo (sem considerar espaços).
#       - Quantas letras tem o primeiro nome.
import os
os.system('cls')

nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())

nome_div = nome.split()
nome_sem_espaco = ''.join(nome_div)

print(f'A quantidade de letras no nome é: {len(nome_sem_espaco)}')
print(f'A quantidade de letras no primeiro nome é: {len(nome_div[0])}')

