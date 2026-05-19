# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
import os
os.system('cls')

v = int(input('Qual a sua velocidade? '))
if v > 80:
    multa = float((v - 80) * 7)
    print(f'Você estava a {v}Km/h, por isso você foi multado! Você deve pagar R${multa:,.2f}')
    