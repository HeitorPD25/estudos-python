# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
import os
os.system('cls')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'{junto} ao contrário é {inverso}')
if junto == inverso:
    print('Temos um Palíndromo.')
else:
    print('Essa frase não é um palíndromo.')