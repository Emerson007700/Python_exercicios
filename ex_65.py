# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n1 = 0
soma = 0
cont = 0
resp = 'S'
maior = 0
menor = 0
while resp in 'Ss':
    n1 = int(input('Digite um numero: '))
    resp = str(input('Quer continuar [S/N: ')).strip().upper()[0]
    soma += n1
    cont += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / cont
print('Voce digitou {} numeros A média dos numeros digitado é {}'.format(cont, media))
print('O Menor numero foi {} e o Maior numro foi {}'.format(menor, maior))



