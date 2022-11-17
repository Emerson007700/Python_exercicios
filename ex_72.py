# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONSE', 'DESE', 'TREZE',
           'QUATORZE', 'QUINZE','DEZESEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    n1 = int(input('Digite um numro: '))
    if n1 > 20:
        print('Tente outro numro')
    else:
        print(f'O numero por extenço é {numeros[n1]}')
        resp = ' '
        while resp not in 'NS':
            resp = str(input('Quer continuar? [ S/N ] ')).strip().upper()[0]
        if resp == 'N':
            break
print('Fim')




