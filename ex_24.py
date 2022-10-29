# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
n1 = str(input('Digite sua cidade: ')).strip()

print('SANTO' in n1[:5].upper()) # O USO DO CONTADOR (n1[:5]) foi pra informar que era paser verdadeso somente se fosse no inicio da frase
