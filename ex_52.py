# Exercício Python 52: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
# OBS: PARA UM NUMERO SER PRIMO ELE SO PODE SER DIVISIVEL 2 OU SEJA POR (1 OU POR ELE MESMO
tot = 0
n1 = int(input('Digite um numero ve veja se ele é primo ou não: '))
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[1;33m ', end=' ') # aqui esta na cor amarela e vai mostrar por quantos numeros o numeo que o usuario digitou é divizivel
        tot = tot + 1 # Aqui tot é um contador e vai falar por quntas veses ele foi divisivel
    else:
        print('\033[1;31m ', end=' ') # aqui esta na cor vermelha e vai mostra por quais numero ele não é divisivel
    print(' {} '.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n1, tot))
if tot == 2:
    print('{} é um numero PRIMO'.format(n1))
else:
    print('{} Não é um numero PRIMO'.format(n1))
