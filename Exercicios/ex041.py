# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia 
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
import os
from datetime import date
os.system('cls')

idade = int(input('Rapaz, que ano vc nasceu? '))
# idade = date.today().year - ano

if idade > 25:
    print('MASTER')
elif idade > 19:
    print('SÊNIOR')
elif idade > 14:
    print('JÚNIOR')
elif idade > 9:
    print('INFANTIL')
else:
    print('MIRIM')