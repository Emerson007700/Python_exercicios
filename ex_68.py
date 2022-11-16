# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
print('='*40)
print('       VAMOS JOGAR PARA OU IMPAR')
print('='*40)
while True:
    jog = int(input('Digite um numro: '))
    comput = randint(0, 10)
    s = jog + comput
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input("Par ou Impara [P/I]: ")).strip().upper()[0]
    print(f'O computador jou {comput} e voce Jogou {jog} a soma é {s}')
    if tipo == 'P':
        if s % 2 == 0:
            print('Voce Venceu')
            cont = cont + 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Voce venceu')
            cont = cont + 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar Novamente')
print(f'Gmae Over! Voce venceu {cont} vezes')




