# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
n1 = int(input('Digite um ano e veja se ele é bissesto: '))
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 ==0:
    print('BISSESTO')
else:
    print('NÃO BISSESTO')