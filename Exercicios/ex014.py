# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
import os
os.system('cls')

celsius = int(input('Digite a temperatura (C°): '))

farenheit = celsius * 1.8 + 32
kelvin = celsius + 273

print(f'''
      ESCALA DE TEMPERATURA
      Celsius: {celsius}C°
      Farenheit: {farenheit}F°
      Kelvin: {kelvin}K
      ''')