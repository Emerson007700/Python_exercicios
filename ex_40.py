# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
media = (n1+n2)/2
if media < 5:
    print('Sua média é {} e você não atingiu a media minima exigida.'.format(media))
elif media >= 5 and media <= 6.9: # Pode fazer de da sguinte forma tb ( 7 > media >= 5 )
    print('Sua média é {} e voce esta de recuperação.'.format(media))
elif media >= 7.0:
    print('Parabens sua média é {} e voce foi aprovado.'.format(media))