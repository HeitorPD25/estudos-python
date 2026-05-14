# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
import os
os.system('cls')

l = float(input('Digite a largura da parede (metros): '))
h = float(input('Digite a altura da parede (metros): '))

área = l * h
tinta = área / 2

print(f'Sendo a altura {h:,.2f}m e a largura {l:,.2f}m, á area da parede é {área:,.2f}m², e vc precisará de {tinta:,.2f} litros de tinta.')
