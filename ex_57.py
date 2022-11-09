# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: ')).strip().upper()[0] # Veja que eliminamos os espaços transformanos em maisculos e
while sexo not in 'MmFf':
    sexo = str(input('Dados invalido. Insira um valor valido (M ou F): '))
print('Sexo {} registrado com sucesso.'.format(sexo))