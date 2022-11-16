while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'M/F':
        sexo = str(input('Sexo: [M/F ')).strip().upper()[0]

    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]

