# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import os
import random
os.system('cls')

pc = ['PEDRA', 'PAPEL', 'TESOURA']
pc_atualizado = random.choice(pc)
 
print('''
       Suas Opções:
       [ 0 ] PEDRA
       [ 1 ] PAPEL
       [ 2 ] TESOURA
       ''')
opt = int(input('Qual é a sua jogada? '))

match opt:
    case 0: # PEDRA
        if pc_atualizado == 'PEDRA':
            print(f'O computador jogou {pc_atualizado}. Deu Empate.')
        elif pc_atualizado == 'PAPEL':
            print(f'O computador jogou {pc_atualizado}. O computador venceu.')
        else: # pc == 'TESOURA'
            print(f'O computador jogou {pc_atualizado}. Você venceu.')
    case 1: # PAPEL
        if pc_atualizado == 'PEDRA':
            print(f'O computador jogou {pc_atualizado}. Você venceu.')
        elif pc_atualizado == 'PAPEL':
            print(f'O computador jogou {pc_atualizado}. Deu Empate.')
        else: # pc == 'TESOURA'
            print(f'O computador jogou {pc_atualizado}. O computador venceu.')
    case 2: # TESOURA
        if pc_atualizado == 'PEDRA':
            print(f'O computador jogou {pc_atualizado}. O computador venceu.')
        elif pc_atualizado == 'PAPEL':
            print(f'O computador jogou {pc_atualizado}. Você venceu.')
        else: # pc == 'TESOURA'
            print(f'O computador jogou {pc_atualizado}. Deu Empate.')