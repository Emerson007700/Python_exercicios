# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year # importar a data atual
ano = int(input('Em que ano você nasceu? '))
soma = atual-ano
if soma == 18:
    print('Esse é ano exato para você se alista pois completa {} anos.'.format(soma))
elif soma < 18:
    print('Ainda falta {} para você se alistar.'.format(18-soma))
elif soma > 18:
    print('Voce passou {} anos do exato momento para se alistar.'.format(soma-18))