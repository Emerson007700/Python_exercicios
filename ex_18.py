import math
a=float(input('Digite o angulo que vc deseja: '))
seno=math.sin(math.radians(a))
coseno=math.cos(math.radians(a))
tange=math.tan(math.radians(a))
print('O anglo de {} tem o seno {:.2f}\nO coseno {:.2f} e\nA tangente {:.2f}'.format(a, seno, coseno, tange))