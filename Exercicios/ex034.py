# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
import os
os.system('cls')

salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    print(f'Seu aumento foi de 10%. Seu salário corrigido é R${salario + salario * 0.10}')
else:
    print(f'Seu aumento foi de 15%. Seu salário corrigido é R${salario + salario * 0.15}')