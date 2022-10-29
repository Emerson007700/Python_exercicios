
# Digite uma frase e transforme toda em maiscula e toda em minuscula e depois conte quantos caracteres tem sem espaços
# Depois mostre quantos caracteres tem o primeiro nome
n1 = str(input('Digite seu nome completo: ')).strip()
print(n1.upper())
print(n1.lower())
print(len(n1) - n1.count(' '))
print(n1.find(' '))




