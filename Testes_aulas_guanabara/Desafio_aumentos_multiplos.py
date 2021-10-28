'''Escreva um programa qe pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento de 15%.'''



salario = float(input('Qual o valor do seu salário? '))
maior = (salario * 0.1) + salario
menor = (salario * 0.15) + salario
if salario <= 1250:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(salario, menor))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f}'.format(salario, maior))