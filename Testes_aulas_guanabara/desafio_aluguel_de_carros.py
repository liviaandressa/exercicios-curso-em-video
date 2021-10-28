# escreva um programa que pergunte a quantiade de Km percorridos po um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0.15 centavor por Km rodado

km = float(input("digite a quantidade de quilometros percorridos: "))
dias = int(input("digite a quatidades de dias: "))
preço = (dias * 60) + (km * 0.15)
print("voce vai ter que pagar {} ".format(preço))
