# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

nome = []
peso = []
while True:
    n = str(input('Nome: '))
    p = int(input('Peso: '))
    nome.append(n)

    resp = str(input('Quer continuar [S/N]? ')).strip()
    if resp in 'Nn':
        break
print(nome)
