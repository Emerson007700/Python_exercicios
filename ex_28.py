# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
print('Pensei em um numer você consegue adivinhar? ')
numero = int(input('Digite um numero: '))
n1 = random.randint(0, 5)
sorteio = n1
if sorteio == numero:
    print('Voce acertou')
else:
    print('Você errou, o numero sorteado foi {}'.format(n1))