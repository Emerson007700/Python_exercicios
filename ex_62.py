# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=" -> ")
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('Fim')