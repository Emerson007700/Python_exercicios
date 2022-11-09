# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair do programa''')
    opçao = float(input('Qual a opção desejada? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma é {}'.format(soma))
    elif opçao == 2:
        mult = n1 * n2
        print('A Multiplicação é {}'.format(mult))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o Maior é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os numeros novamente')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opçao == 5:
        print('Até mais')
    else:
        print('Tente outra opão')
    print('-=-' * 10)
    sleep(2)
print('Fim')



