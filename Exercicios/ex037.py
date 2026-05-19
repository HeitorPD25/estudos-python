import os 
os.system('cls')

num = int(input('Digite um número: '))
print("""
         MENU DE CONVERÇÃO:
         1 -> Binário
         2 -> Octal
         3 -> Hexadecimal
         """)
opcao = int(input('Digite sua escolha: '))

if opcao == 1:
    print(f'O número {num} em binário é {format(num, 'b')}')
elif opcao == 2:
    print(f'O número {num} em octal é {format(num, 'o')}')
elif opcao == 3:
    print(f'O número {num} em hexadecimal é {format(num, 'x')}')
else:
    print('Não existe essa opção. Não quebre o sistema, meu camarada.')
