'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''


peso = float(input('Informe seu peso: '))
altura =  float(input('Informe sua altura: '))
calculo = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(calculo))
if calculo < 18.5:
    print('Abaixo do peso')
elif calculo >= 1.85 and calculo < 25:
    print('Peso ideal')
elif calculo >= 25 and calculo < 30:
    print('Sobrepeso')
elif calculo >= 30 and calculo < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')