n1=float(input('Informe um valor e veja quanto de desconto voceterá: R$ '))
n2=float(input('Informe o quanto (%) de desconto voce quer e veja o resultado: '))
s=n1-(n1/100)*n2

print('O valor com desconto é de R${:.2f} reais'.format(s))