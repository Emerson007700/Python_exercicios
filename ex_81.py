# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = cont + 1
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'Voce digitou {cont} numeros')
print(f'Veja sua lista em ordem decrescente {lista}')
if 5 in lista:
    print('O numero 5 esta na sua lista:')
else:
    print('O numero 5 não se enconta na sua lista')
