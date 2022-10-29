# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
n1 = str(input('Escre uma frase: ')).upper().strip() # ja voi passado para o maiusculo aqui
print(n1.count('A'))
print(n1.find('A') + 1) # foi adicionado o mais um para visulizacao do usuario pois ele conta apartir de (0)
print(n1.rfind('A')+1)
