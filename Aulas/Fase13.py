# ESTRUTURA DE REPETIÇÃO FOR
for c in range(0, 6): # Conta de 0 à 5
    print(c)
print('FIM')

for c in range(1, 7): # Conta de 1 à 6
    print(c)
print('FIM')

for c in range(6, 0, -1): # Conta para trás de 6 à 1
    print(c)
print('FIM')

for c in range(0, 7, 2): # Conta de 0 à 6 pulando de 2 em 2
    print(c)
print('FIM')

# ===================================================================
n = int(input('Digite um número')) # Esse programa faz a contagem até onde o usuário escolher.
for c in range(0, n+1):
    print(c)
print('FIM')

# ===================================================================
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(f'A Soma de todos os valores foi {s}')
