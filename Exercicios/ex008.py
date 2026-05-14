# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite a sua metragem: '))

cent = metros * 100
milim = metros * 1000

print(f'''
      Metro: {metros}
      Centímetros: {cent}
      Milímetros: {milim}
      ''')