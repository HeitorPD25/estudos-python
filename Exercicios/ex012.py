# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
import os
os.system('cls')

preco = float(input('Digite o preço: R$'))
desc = preco - (preco * 0.05)

print(f'O preço era R${preco}, com desconto de 5% fica R${desc}')