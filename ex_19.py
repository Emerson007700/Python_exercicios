import random

n1 = input('Diga seu nome: ')
n2 = input('Diga seu nome: ')
n3 = input('Diga seu nome: ')
n4 = input('Diga seu nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
