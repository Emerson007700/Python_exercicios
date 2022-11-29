# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2:
        impar.append(n)
    else:
        par.append(n)
    resp = str(input('Quer continuar [S/N]? ' )).strip()
    if resp in 'Nn':
        break
print(f'Su lista é {lista}')
print(f'Os numeros paras são: {par}')
print(f'Os números ímpares são: {impar}')

