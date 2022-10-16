
import math
c1=float(input('Comprimento do cateto oposto: '))
s1=float(input('Comprimento cateto adjacente: '))
h1=math.hypot(c1, s1)
print('A hipotenusa é {:.2f}'.format(h1))


c=float(input('Comprimento do cateto oposto: '))
s=float(input('Comprimento cateto adjacente: '))
h1=(c**2 + s**2)**(1/2)
print('A hipotenusa é {:.2f}'.format(h1))