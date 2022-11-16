# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = s = 0
while True:
    n1 = int(input('Digite um numero e digite (999) para parar: '))
    if n1 == 999:
        break
    cont += 1
    s += n1
print(f'Foram digitados {cont} e a soma deles é {s}')