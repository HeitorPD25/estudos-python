# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import os
import random
os.system('cls')

alunos = ['João', 'Maria', 'José', 'Claúdia']
print(random.choice(alunos))