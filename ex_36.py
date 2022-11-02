# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.
print('-=-'*10)
print('FINANCIAMNETO IMOBILIARIO')
print('-=-'*10)
nome = str(input('Qual seu nome? '))
imovel = float(input('Qual o valor do imovel a ser financiado? '))
salario = float(input('Qual o seu salario? '))
ano = float(input('Em quantos anos você pretende pagar? '))
soma = salario/100*30
soma2 = ano*12
soma3 = (imovel/soma2)
if soma <= soma3:
    print('Seu salario não comporta esse tipo de financimento.')
else:
    print('Parabens seu financiamento foi aprovado.')
print('Bom dia {}.'.format(nome))
