# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo
from math import factorial
n1 = int(input('Qual seu numero: '))
f = factorial(n1)
c = n1
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ',end=' ') # foi usado para colocar o x entre os numeros e o = no final
    c = c - 1
print(f)

