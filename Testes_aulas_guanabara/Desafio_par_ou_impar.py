'''Crie um programa que leia um n´mero inteiro e mostre na tela se ele é par ou ímpar'''

numero = int(input('Me diga um número qualquer: '))
if numero %2 == 0:
    print(' O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))