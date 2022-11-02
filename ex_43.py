# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/ (altura*altura)
if imc < 18.5:
    print('Seu IMC é {:.2f} e esta abaixo de 18,5: Abaixo do Peso'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f} e esta no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f} e esta com sobre peso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.2f} e esta com Obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e esta com Obesidade Morbida.'.format(imc))

