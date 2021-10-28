#faça um programa que leia um número e mostre na tela o seu sucessor e o seu antecessor

numero = int(input("digite um número: "))
ant = numero-1
suc = numero+1
print("o antecessor de {} é {} e o sucessor é {}".format(numero, ant, suc))