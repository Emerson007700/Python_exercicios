# Exercício Python 33: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))

