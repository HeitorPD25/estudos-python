import os # Importa a biblioteca os
os.system('cls') # Limpa o terminal, caso for usado em MacOS ou Linus o comando seria os.system('clear')

# Tipos Primitivos

int # Números inteiros, sejam positivos ou negativos (Ex.: 7, -4, 0, 9875)
float # Números reais, sejam positivos ou negativos (Ex.: 4.5, 0.076, -15.223, 7.0)
bool # Apenas aceita dois valores (Ex.: True / False)
str # Qualquer forma de texto, sempre vai estar entre áspas (Ex.: 'Olá', '7.5', '')

# O método input() sempre vai receber por padrão uma str. Para mudarmos isso precisamos fazer um casting.
n1 = input("Digite um número: ")
print(type(n1)) # O método type() mostra o tipo da variável.
print(n1)

# CASTING
n2 = int(input('Digite um número: '))
print(type(n2))
print(n2)