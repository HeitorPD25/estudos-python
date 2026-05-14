# Manipulando cadeias de texto
frase = 'Curso em Vídeo Python'

# Fatiamento de Strings
print(frase[9]) # Imprime o caracter 9
print(frase[9:13]) # Imprime os caracteres de 9 a 13, excluindo o 13
print(frase[9:21]) # Mesmo não tendo o caracter 21 ele imprime até o 20
print(frase[9:21:2]) # Faz igual em cima mas pulando de dois em dois
print(frase[:5]) # Imprime do começo ao caracter 5
print(frase[15:]) # Imprime do caracter 15 ao final
print(frase[9::3]) # Começa no caracter 9, vai até o final, pulando de 3 em 3

print()
# Análise de Strings
print(len(frase)) # Mostra o comprimento da String
print(frase.count('o')) # Mostra quantas vezes aparece 'o'
print(frase.count('o', 0, 13)) # Igual ao anterior, mas dentro de um intervalo
print(frase.find('deo')) # Mostra quantas vezes ele encontrou 'deo'
print(frase.find('Android')) # Se a String não existir ele retorna -1
print('Curso' in frase) # Existe Curso em frase? Retorna True ou False

print()
# Transformação de Strings
print(frase.replace('Python', 'Android')) # Substitui a primeira pela segunda
print(frase.upper()) # Colocar todas as letras em maiúsculo
print(frase.lower()) # Colocar todas as letras em minúsculo
print(frase.capitalize()) # Colocar a primeira letra da String em maiúscula
print(frase.title()) # Colocar a primeira letra de cada palavra em maiúscula
print(frase.strip()) # Remove todos os espaços no ínicio e no final da String
print(frase.rstrip()) # Remover todos os espaços no final da String
print(frase.lstrip()) # Remover todos os espaços no início da String

print()
# Divisão de Strings
print(frase.split()) # Sem parâmetro, ele divide a String em todos os espaços
frase1 = frase.split()
print('-'.join(frase1)) # Junta todas as partes de frase separadas por -
