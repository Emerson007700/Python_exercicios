# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    n1 = int(input('Digite o {}º numereo: '.format(c)))
    if n1 % 2 == 0:
        soma = soma + n1
print('A soma dos numeros pares é {}'.format(soma))

