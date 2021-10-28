# Faça um programa qeu leia o preço de algum produto e mostre seu novo preço, com 5% de desconto

produto = float(input("digite o preço do produto: "))
desconto = produto * 0.05
novo_valor = produto - desconto
print(" o  novo valor é {:.2f}".format(novo_valor))

#novo_valor =  produto - (produto * 5 / 100) ----- outra forma de calcular