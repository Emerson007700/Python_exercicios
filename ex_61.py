# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.
'''primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao # essa é a formula para ir ate o decimo termo
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=" -> ")
print('ACABOU')'''

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 0
while cont <= 10:
    print('{}'.format(termo), end=" -> ")
    termo = termo + razao
    cont = cont + 1