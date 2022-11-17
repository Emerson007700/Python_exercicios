# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('='*43)
print(f'{"LISTA DE MATRIAL ESCOLAR":^43}') # Para formatar celtralizado
print('='*43)
"""lista = ('Lapis....................R$  3,00', 'Papel....................R$  5,00','Caneta...................R$  3,00',
         'Borracha.................R$  7,00', 'Tesoura..................R$ 10,00','Caderno..................R$ 30,00',
         'Marca Texto..............R$ 15,00', 'Corretivo................R$  3,00','Régua....................R$  5,00')"""
lista = ('Lapis', 3 ,'Papel', 5, 'Caneta', 3, 'Borracha', 7, 'Tesoura', 10, 'Caderno', 30)
for item in range(0, len(lista)):
    if item % 2 == 0: # vai mostar os elementos na posição do indice par
        print(f'{lista[item]:.<33}',end=' ')
    else:
        print(f'R$ {lista[item]:>3.2f}')
print('='*43)






