# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
from random import randint
computador = randint(0, 10)
print('Sou o Computador, Pensei em um numero entre (0, 10)')
print('Voce consegue adivinhar? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual numero pensei? '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Acertou com {} Palpites'.format(palpite))






