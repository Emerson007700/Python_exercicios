# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10)) # sortear vairios elementos
print(f'Os numerso Gerados foram: {numeros}')
print(f'O maior numero foi {max(numeros)} e o menor numero foi {min(numeros)}') # Mostrar o maior e o menor
