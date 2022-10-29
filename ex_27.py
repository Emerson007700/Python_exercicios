# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

n1 = str(input('Digite seu nome completo: ')).strip()
primeiro  = n1.split()[0]
print(' '.join(primeiro))

ultimo = n1.split()[-1]
print(' '.join(ultimo))
