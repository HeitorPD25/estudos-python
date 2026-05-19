import os
os.system('cls')

n1 = int(input('Digite o número 01: ')) 
n2 = int(input('Digite o número 02: '))

if n1 > n2:
    print(f'Cara, não sei se vc sabe, mas {n1} é maior que {n2}')
elif n2 > n1:
    print(f'Cara, não sei se vc sabe, mas {n2} é maior que {n1}')
else:
    print(f'Cara, não sei se vc sabe, mas {n1} é igual a {n2}')