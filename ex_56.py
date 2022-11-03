# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
soma = 0
cont = 0
maior = 0
menor = ''
for c in range(1,5):
    nome = str(input('Qual o nome da {}º pessoa? '.format(c)))
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo (M) OU (F)? ')).upper()
    print('-=-' *12)
    soma = (soma + idade)
    if sexo == 'M':
        if c == 1:
            maior = idade
            menor = idade
        else:
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade
        sexo = nome
        homem = sexo
        print(sexo)
    elif sexo == 'F':
        sexo = nome
        mulher = sexo
        if idade < 20:
            cont = cont + 1
        print(sexo)
    else:
        print('Opão invalida tente (M) OU (F)' )
print('A média de idade do grupoe é {} anos\n'
      '{} é o homem mais velho\n'
      'O grupo pussui {} mulheres abaixo de 20 anos'.format(soma/c,homem, cont))


