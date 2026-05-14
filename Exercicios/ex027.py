# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.
import os
os.system('cls')

nome = str(input('Digite seu nome completo: ')).strip()
nome_div = nome.split()
print(f'Seu primeiro nome é: {nome_div[0]}')
print(f'Seu último nome é: {nome_div[len(nome_div)-1]}')