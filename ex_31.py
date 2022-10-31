# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
v = float(input('Qual a distancia da sua viagem? '))

if v <= 200:
    print('Sua passagem custará {:.2f}'.format(v*0.50))
else:
    print('Passagem custará R$ {:.2f}'.format(v*0.45))
