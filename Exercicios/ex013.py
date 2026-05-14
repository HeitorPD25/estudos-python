# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
import os
os.system('cls')

salario = float(input('Digite seu salário: R$'))
aumento = salario + (salario * 0.15)
print(f'Parabéns! Seu salário era {salario}, mas você ganhou 15% de aumento, logo seu salário agora é {aumento}')
