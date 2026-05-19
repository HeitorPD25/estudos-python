# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.
import os
os.system('cls')

n = int(input('Digite um número para sua tabuada: '))
os.system('cls')
print((f'TABUADA DO {n}:'))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')