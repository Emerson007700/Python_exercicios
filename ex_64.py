# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
cont = 0
soma = 0 # A SOMA VAI TECEBER TODA VEZ A SOMA DO N E VAI ARMAZENAR E TODA VEZ VAI SOMAR COM PROXIMO NUMERO DIGITADO
n = int(input('Digite um numero e para parara digite (999): ')) # OBS(PARA NÃO SOMAR O (999) DIGITADO PELO USUARIO E PRECISO COLOCAR AQUI FORA DO WHILE E NA ULTIMA LINHA REPETIR ESSE COMANDO VEJA
while n != 999:
    soma  = soma + n
    cont = cont + 1
    n = int(input('Digite um numero e para parara digite (999): ')) # REPETI AQUI O COMANDO DE ENTRADA PARA NAO SOMAR AOS NUMEROS DIGITADOS (ganbiarra kkkk)
print('Fim. foram digitados {} numeros a soma foi {}'.format(cont, soma))

