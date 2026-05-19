import os
from datetime import date
os.system('cls')

ano = int(input('Rapaz, que ano vc nasceu? '))
idade = date.today().year - ano

if idade < 16:
    if (16 - idade) > 1:
        print(f'Parabéns! Vc ainda não precisa ir para a guerra. Faltam {16 - idade} anos.')
    else:
        print(f'Parabéns! Vc ainda não precisa ir para a guerra. Faltam {16 - idade} ano.')
elif idade <= 18:
    print('Cara, sinto muito. Mas vc precisa ir se alistar pra guerra.')
else:
    if (idade - 18) > 1:
        print(f'MANO!!! Vc já devia ter se alistado. Já se passaram {idade - 18} anos do prazo.')
    else:
        print(f'MANO!!! Vc já devia ter se alistado. Já se passaram {idade - 18} ano do prazo.')
