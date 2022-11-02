# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
p = float(input('Qual o valor do seu produto? '))
print('''Escolha as as formas de pagamento asseguir:
[ 1 ] Para gamento avista dinheiro/cheque 10 % de desconto.
[ 2 ] Para pagamento à vista no cartão: 5% de desconto.
[ 3 ] Para pagamento em até 2x no cartão: preço formal 
[ 4 ] Para pagamento 3x ou mais no cartão: 20% de juros''')
pagamento = int(input('Digite a opçao desejada: '))
av = p-(p/100*10)
ac = p-(p/100*5)
pc = p+(p/100*20)
if pagamento == 1:
    print('Avista Dinheiro voce irá pagar R$ {:.2f}'.format(av))
elif pagamento == 2:
    print('Avista Cartão Voce irá pagar R$ {:.2f}'.format(ac))
elif pagamento == 3:
    print('Pagamento parcelado em 2 x R$ {:.2f}'.format(p))
elif pagamento == 4:
    tp = int(input('Ou digite o total de parcelas: '))
    print('Seu Pagamento parcelado sera R$ {:.2f} em {} em parcelas é de R$ {:.2f}'.format(pc,tp, pc/tp))
else:
    print('Opção Invalida tente uma das opçoes acima.')

