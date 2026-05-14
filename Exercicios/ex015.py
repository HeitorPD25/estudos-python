# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
# alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
import os
os.system('cls')

dia = int(input('Digite quantos dias ficou com o carro: '))
km = float(input('Digite quantos km andou com o carro: '))

valor_dia = dia * 60
valor_km = km * 0.15
valor_total = valor_km + valor_dia

print(f'''
      VALOR DO ALUGUEL:
      Diárias: R${valor_dia}
      Quilometragem: R${valor_km}
      TOTAL: R${valor_total}
      ''')