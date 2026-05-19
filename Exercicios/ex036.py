import os
os.system('cls')

casa = float(input('Digite o valor da Casa: R$'))
salario = float(input('Digite seu salario: R$'))
anos = int(input('Em quantos anos você deseja pagar: '))
parcela = casa / (anos*12)

if parcela > (salario*0.30):
    os.system('cls')
    print(f'Infelizmente com o seu salário de R${salario}, você não poderá pagar a parcela de R${parcela:,.2f}')
else:
    os.system('cls')
    print(f'Parabéns! Seu empréstimo foi aprovado. Sua parcela será de R${parcela:,.2f}, e você deverá pagar em {anos} anos')