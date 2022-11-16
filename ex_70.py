# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
tot = totmais = totbarato = cont = 0
prodbarato = ' '
while True:
    prod = str(input('Qual é o produto? '))
    preço = float(input('Qual o preço do produto? '))
    cont = cont + 1
    tot = tot + preço
    if preço > 1000:
        totmais = totmais + 1
    if cont == 1:
        totbarato = preço
        prodbarato = prod
    else:
        if preço < totbarato:
            totbarato = preço
            prodbarato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'RS {tot :.2f} Foram gastos nessa compra.')
print(f'{totmais} Custaram mais de R$ 1.000,00.')
print(f'{prodbarato} Foi o Produto mais barato e custa R$ {totbarato :.2f}.')
