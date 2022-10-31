import math
import random

n1 = random.randint(0, 120)
s = n1
if n1 <= 80:
    print("Sua velocidade é {} km/h você esta no limite permitido".format(n1))
else:
    print('Sua velocidade foi {} km/h e esta acima do permitido então receberá uma multa de R$ {:.2f} '.format(n1, (s-80)*7))