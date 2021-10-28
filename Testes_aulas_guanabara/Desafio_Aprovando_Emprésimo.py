'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte  valor da casa, o salário d cmprador e em quantos ans ele vai pagar.
A prestação mensal não ode exceder 30% do salário ou então o empréstom será negado'''


valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento: '))
minimo = salario * 0.30
prestaçao = valor_casa / (anos * 12) #o valor da casa dividido em quantos meses ele vai pagar
print('Para uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor_casa,anos, prestaçao))
if prestaçao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('LARGA DE SER TROUXA QUE TU NÃO PODE PAGAR UMA CASA NESSE VALOR! ')


#print('comparando  tem que pagar {} e o minimo é de {}'.format(prestaçao, minimo))

