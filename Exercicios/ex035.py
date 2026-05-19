# Exercício Python 035: Desenvolva um programa que leia o comprimento de 
# três retas e diga ao usuário se elas podem ou não formar um triângulo.
import os
os.system('cls')

a = int(input('Valor da reta a: '))
b = int(input('Valor da reta b: '))
c = int(input('Valor da reta c: '))

if a + b > c and b + c > a and c + a > b:
    print('Podem formar um triângulo.')
else:
    print('Não podem ser triângulos.')