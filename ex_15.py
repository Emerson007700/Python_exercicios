import random

d=float(input("Quantos dias você alugou o carro? "))
km=float(input('Quantos KM você rodou? '))
s=(60*d)+(km*0.15)

print('Você tem que pagar {:.2f}'.format(s))

