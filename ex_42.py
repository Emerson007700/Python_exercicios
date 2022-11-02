# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
print('-=-'*10)
print('Analizando triangulos')
print('-=-'*10)

r1 = float(input('Pirmeira reta: '))
r2 = float(input('Sefunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas formam um triangulo')
    if r1 == r2 and r2 == r3:   # O PYTHON tb aceita ( r1 == r2 == r3) essa comparação
        print('Triangulo EQUILÁTERO: Pois todos os lados são iguais')
    elif r1 != r2 != r3 !=r1:
        print('Tringulo ESCALENO: Pois os TRES lados são diferente')
    else:
        print('Tringulo ISOCELES: Pois DOIS lados sao iguais e um diferente')


else:
    print('Retas não formam um triangulo')