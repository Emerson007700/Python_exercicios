# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nascimento = int(input('Qual a data de seu nascimento? '))
idade = atual-nascimento
if idade <= 9:
    print('Sua iade é {} anos e voce esta na categoria Mirin.'.format(idade))
elif 9 < idade <= 14:
    print('Sua iade é {} anos e voce esta na categoria Infatil'.format(idade))
elif 14 < idade <= 19:
    print('Sua iade é {} anos e voce esta na categoria Junior'.format(idade))
elif 19 < idade <= 25:
    print('Sua iade é {} anos e voce esta na categoria Senior'.format(idade))
elif idade > 25:
    print('Sua iade é {} anos e voce esta na categoria Master'.format(idade))
print(idade)

