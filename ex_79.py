# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.
val = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in val:
        val.append(numero)
    else:
        print('Esse é um numero repetido, por favor digite outro numero.')
    cond = str(input('Quer continuar [S/N]? ')).strip()
    if cond in 'Nn':
        break
val.sort()
print(f'Sua lista é {val}')