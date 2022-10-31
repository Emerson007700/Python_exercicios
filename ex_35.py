# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*10)
print('Analizando triangulos')
print('-=-'*10)

r1 = float(input('Pirmeira reta: '))
r2 = float(input('Sefunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas formam um triangulo')
else:
    print('Retas não formam um triangulo')