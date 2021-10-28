'''Faça um programa que leia três nmeros e mostre qual é o maior e o menor'''

numero1 = int(input('digite um número: '))
numero2 = int(input('digite um número: '))
numero3 = int(input('digite um número: '))

menor =  numero1
if numero2<numero1 and numero2<numero3:
    menor= numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3
print('O menor é o número {}'.format(menor))

maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3
print('O maior é o número {} '.format(maior))

