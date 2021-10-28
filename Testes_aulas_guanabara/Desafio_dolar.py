#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

#dolar: us 1.00= 5.60


carteira =  float(input("quanto dinheiro você tem na carteira: "))
conversao = carteira/5.60
print("voce pode compar {:.2f} dolares".format(conversao))
