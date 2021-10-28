#Faça um programa que leia um Ângul qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

import math

angulo = int(input("digite um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("o seno de {} é igual a {:.2f}, o cosseno vale {:.2f}, e a tangente vale {:.2f}".format(angulo, seno, cosseno, tangente))