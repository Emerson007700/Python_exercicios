somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
totmulher = 0
for p in range(1, 5):
    nome = str(input('Qual o nome da {}º pessoa? '.format(p))).strip()
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo (M) OU (F)? ')).strip()
    print('-=-' * 15)
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade/4
print('A média da idade é {}'.format(mediaidade))
print('O home mais velho é {}'.format(nomevelho))
print("O total de mulheres com menos de 20 anos é  {}".format(totmulher))

