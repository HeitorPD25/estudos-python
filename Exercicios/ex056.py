# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.
import os
os.system('cls')

soma_idades = 0
nome_mais_velho = 0
idade_mais_velho = 0
mulher = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: '))
    
    idade = int(input('Idade: '))
    soma_idades += idade
    
    sexo = str(input('Sexo [M/F]: '))
    if sexo == 'F' and idade <= 20:
        mulher += 1
    
    if sexo == 'M':
        if i == 1:
            nome_mais_velho = nome
            idade_mais_velho = idade
        else:
            if idade > idade_mais_velho:
                nome_mais_velho = nome
                idade_mais_velho = idade

media = soma_idades/4
print(f'A média de idade do grupo é de {media:,.1f} anos.')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')
