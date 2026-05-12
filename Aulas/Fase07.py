import os
os.system('cls')

# Operadores Aritméticos

print('Operadores Aritméticos')
print(2 + 3)  # SOMA (Res.: 5)
print(2 - 3)  # SUBTRAÇÃO (Res.: -1)
print(2 * 3)  # MULTIPLICAÇÃO (Res.: 6)
print(2 / 3)  # DIVISÃO (Res.: 0.6666...)
print(2 ** 3) # POTÊNCIA (Res.: 8)
print(2 // 3) # DIVISÃO INTEIRA (Res.: 0)
print(2 % 3)  # MÓDULO (Res.: 2)

# Ordem de Procedência
# 1 -> ()
# 2 -> **
# 3 -> * | / | // | %
# 4 -> + | -

exemplo1 = 5 + 3 * 2
exemplo2 = 3 * 5 + 4 ** 2
exemplo3 = 3 * (5 + 4) ** 2

print()
print('Ordem de Procedência')
print(f'5 + 3 * 2 = {exemplo1}')
print(f'3 * 5 + 4 ** 2 = {exemplo2}')
print(f'3 * (5 + 4) ** 2 = {exemplo3}')