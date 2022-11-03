# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao # essa é a formula para ir ate o decimo termo
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=" -> ")
print('ACABOU')