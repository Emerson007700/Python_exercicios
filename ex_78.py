# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
val = []
maior = 0
menor = 0
pos = 0
for c in range(0, 6):
    val.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = val[c]
    else:
        if val[c] > maior:
            maior = val[c]
        if val[c] < menor:
            menor = val[c]
print(f'Voce digitou os numeros: {val}')
print(f'O Maior número é {maior} na posição ',end='')
for i, v in enumerate(val):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O Menor número é {menor} na posição ',end='')
for i, v in enumerate(val):
    if v == menor:
        print(f'{i}...', end='')
print()


