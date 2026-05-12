# DESAFIO 004 - Faça um programa que leia algo pelo teclado e mostre na tela
#               o seu tipo primitivo e todas as informações possíveis sobre ele.

import os
os.system('cls')

var = input('Digite algo: ')
print(f'O tipo da sua variável é {type(var)}')
print(f'Só tem espaços? {var.isspace()}') 
print(f'É um número? {var.isnumeric()}')
print(f'É alfabético? {var.isalpha()}')
print(f'É alfanúmerico? {var.isalnum()}')
print(f'Está em maiúsculas? {var.isupper()}')
print(f'Está em minúsculas? {var.islower()}')
print(f'Está capitalizada? {var.istitle()}')
