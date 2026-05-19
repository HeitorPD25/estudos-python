# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na 
# tela se o usuário venceu ou perdeu.
import os
import random
os.system('cls')

print('VOU PENSAR EM UM NÚMERO DE 0 A 5. TENTE ADVINHAR...')
num = random.randint(0, 5)
chute = int(input('Em que número eu pensei? '))

if chute == num:
    print(f'Parabéns! Você chutou {chute}, e meu número era {num}')
else:
    print(f'Sinto Muito! Você chutou {chute}, e meu número era {num}')