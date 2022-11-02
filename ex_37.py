# Exercício Python 37: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero inteiro: '))
print(' Digite (1) para Binario \n Digite (2) para Octal \n Digite (3) para Hexadecimal')
n1 = int(input('Digite a opçao desejada: '))
if n1 == 1:
    print('O numero em binario é: {}'.format(bin(numero)[2:]))
elif n1 == 2:
    print('O num em octal é {}'.format(oct(numero)[2:]))
elif n1 == 3:
    print('O numero em hexadecimal é {}'.format(hex(numero)[2:]))
else:
    print('Opção invalida tente uma das opçoes acima.')
