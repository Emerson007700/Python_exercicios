n1 = int(input('Dige um numere ente 1 e 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('A Unidadade é {}'.format(u))
print('A Dezena é {}'.format(d))
print('A Centena é {}'.format(c))
print('O Milhar é {}'.format(m))
