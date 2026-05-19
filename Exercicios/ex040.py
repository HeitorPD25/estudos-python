# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#   Média abaixo de 5.0: REPROVADO
#   Média entre 5.0 e 6.9: RECUPERAÇÃO
#   Média 7.0 ou superior: APROVADO
import os
os.system('cls')

n1 = float(input('Digite sua nota 01: '))
n2 = float(input('Digite sua nota 02: '))
m = (n1 + n2) / 2

if m < 5.0:
    print(f'Sua média é {m}. Você foi REPROVADO.')
elif m < 7.0:
    print(f'Sua média é {m}. Você está de RECUPERAÇÃO.')
else:
    print(f'Sua média é {m}. Você foi APROVADO.')