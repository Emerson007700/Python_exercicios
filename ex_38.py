# Exercício Python 038: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite segundo numero: '))
if n1 > n2:
    maior= n1
    print('O prineiro é maior que o segundo numero'.format(maior))
elif n2 > n1:
    maior = n2
    print('O segundo numero é maior que o primeiro numero digitado'.format(maior))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')