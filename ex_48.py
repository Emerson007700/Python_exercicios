# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
soma = 0 # Essa Variavel é um acumulador que geralmente somo os valores encontrados
cont = 0 # Essa variavel vai contar ele é um (contador +1) quantos numeros foram usados nessa conta
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1  # O ( + 1 ) e para informar q toda vez q encontrar um numero ele vai contar
        soma = soma + c # veja a identação
print('Foram encontrados \033[1;35m{}\033[m divisiveis por 3 e a soma entre ele é \033[1;35m{}\033[m'.format(cont, soma))