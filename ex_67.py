# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-=-'*16)
    n1 = int(input('Quer saber a tabuado de qual numero? '))
    print('--'*12)
    if n1 < 0:
        break
    for c in range(0, 10):
        c = c + 1
        s = c * n1
        print(f'I     {c} x {n1} = {s}     I ')
print('-=-'*16)
print('Essa tabuada não le numeros negativos fim de programa')

