# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros
import os
os.system('cls')

preco = float(input('Digite o valor da compra: '))
print("""
      ESCOLHA SUA FORMA DE PAGAMENTO:
      1. à vista dinheiro/cheque: 10% de desconto
      2. à vista no cartão: 5% de desconto
      3. em até 2x no cartão: preço formal
      4. 3x ou mais no cartão: 20% de juros    
      """)
opt = int(input('Qual a opção de pagamento? '))

match opt:
    case 1:
        preco_1 = preco - preco * 0.10 
        print(f'Você ganhou 10% de desconto. Sua compra ficou R${preco_1:,.2f}')
    case 2:
        preco_2 = preco - preco * 0.05
        print(f'Você ganhou 5% de desconto. Sua compra ficou R${preco_2:,.2f}')
    case 3:
        parc_3 = preco / 2
        print(f'O seu valor continua R${preco}. Você vai pagar 2 parcelas de R${parc_3:,.2f}')
    case 4:
        parc_4 = preco / 3
        print(f'O seu valor continua R${preco}. Você vai pagar 2 parcelas de R${parc_4:,.2f}')
    case _:
        print('Essa opção não existe.')