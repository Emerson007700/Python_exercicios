# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
n1 = str(input('Digite uma frase e veja ela de tras pra frente: ')).strip().upper()
palavras = n1.split() # Fez um split para gerar uma lista
junto = ' '.join(palavras) # aqui nuntou tudo em uma unica string
inverso = ''
inverso = junto[::-1] # essa versao sem for muito melhor
'''for c in range(len(junto) -1, - 1, -1):
    inverso = inverso + junto[c]'''
if inverso == junto:
    print('Palindromo')
else:
    print('Nao Palondromo')


