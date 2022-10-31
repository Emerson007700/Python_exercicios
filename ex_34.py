# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n1 = float(input('Qual o seu salario? '))
if n1 >= 1250:
    print('Seu salario atual apos o aumento é {:.2f}'.format((n1/100)*10 + n1))
else:
    print('Seu salario atual apos o aumento é {:.2f}'.format((n1/100)*15 + n1))

