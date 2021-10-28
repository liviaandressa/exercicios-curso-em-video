# Faça um programa que elia um número inteiro qualquer e mostre na tabela a sua tabuada

numero = int(input("tabuada de: "))
contador = 0
while contador <= 10:
    tabuada = numero * contador
    print("{}x{} ={}".format(numero, contador, tabuada))
    contador += 1
