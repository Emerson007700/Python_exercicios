# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
lista = ('Lapis', 'Papel', 'Caneta', 'Borracha', 'Tesoura', 'Caderno')
for item in lista:
    print(f'\nNa palavra {item} tem as vogais: ', end=" ")
    for vog in item:
        if vog.lower() in 'aeiou': # se usou o lower para transforamr em minuscula
            print(vog, end=' ')


