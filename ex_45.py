from random import randint
# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

print('-=-'* 15)
print('        ----VAMOS JOGAR JOKENPÔ----')
print('-=-'* 15)
n1 = input('VAMOS LÁ QUAL SEU NOME? ')
print('''OLÁ {} EU SOU RODRIGO A INTELIGENCIA ARTIFICIAL DO JOGO
SEJA BEM VINDO A JOGO JOKENPÔ, TENHA UMA BOA SORTE!!!!!!!!!!'''.format(n1))
print(''' ESCOLHA ENTRE AS OPÇOES ABAIXO
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jg = int(input("O QUE VC ESCOLHE: "))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('{} ESCOLHEU [ {} ]'.format(n1, itens[jg]))
print('\033[1;31mRODRIGO ESCOLHEU\033[m [ {} ]'.format(itens[cpu]))
if cpu == 0:
    if jg == 0:
        print('EMPATE')
    elif jg == 1:
        print('---=== {} GANHOU ===---'.format(n1))
    elif jg == 2:
        print('---=== RODRIGO GANHOU ===---'.format())
    else:
        print('---=== JOGADA INVALIDA ===---')

elif cpu == 1:
    if jg == 0:
        print('RODRIGO GANHOU')
    elif jg == 1:
        print('EMPATOU')
    elif jg == 2:
        print('{} GANHOU'.format(n1))
    else:
        print('JOGADA INVALIDA')

elif cpu == 2:
    if jg == 0:
        print('{} GANHOU'.format(n1))
    elif jg == 1:
        print('RODRIGO GANHOU')
    elif jg == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVALIDA')
else:
    print('Fim de Jogo')


