# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numero = []
for c in range(0, 5):
    n = int(input(f'Digite um numero a pisição dele é {c}:  '))
    if c == 0 or n > numero[-1]:
        numero.append(n)
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
                numero.insert(pos, n)
                break
            pos += 1
print(f'A lista em oredem é {numero}')

