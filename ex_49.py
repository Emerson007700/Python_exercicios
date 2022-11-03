# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
n1 = int(input('Qual a tabuada que vc quer saber: '))
for c in range(1 , 11):
    print('{} x {} = {}'.format(n1, c,n1*c))