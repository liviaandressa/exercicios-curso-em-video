''' Escreva um programa que leia dois números inteiros e compare- os. mostrando na trla a mensagem:
 - O primeiro valor é maior
 - O segundo valor é aior
 - Não existe valor maior, os dois são iguais'''

valor1 = int(input('Primeiro número: '))
valor2 = int(input('Segundo número: '))

if valor1 > valor2:
    print('O primeiro valor é maior')
elif valor2 > valor1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dos valores são iguais.')