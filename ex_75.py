# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = (int(input('Digite o primeiro numero: ')), # essa é uma variavel composta tipo TUPLA
           int(input('Digite o segundo numero: ')),
           int(input('Digite o terceiro numero: ')),
           int(input('Digite o quarto numero: ')))
print(numeros)
print(f'Quantas vezes apareceu o valor 9? {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O Numero 3 foi digitado na {numeros.index(3)+1} posição')
else:
    print('O numero 3 não foi digitado nenhuma vez.')
print('Os numeros pares foram: ', end=" ")
for n in numeros:
    if n % 2 == 0:
        print(n, end=' - ')
