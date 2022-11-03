# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
cont = 0
cont2 = 0
atual = date.today().year
for c in range(0,6+1):
    idade = int(input('Qual o ano de seu nascimento? '))
    soma = atual - idade

    if soma >= 18:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print('{} Já sao maiores de idade. {} Ainda nao atingiram a mair idade'.format(cont, cont2))





