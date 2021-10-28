#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãgulo retângulo, calcule e mostre mostre o comrimento da hipotensa.

import math

c_oposto = float(input("digite o comprimento do cateto hoposto: "))
c_adjacente = float(input("Digite o comprimeno do cateto adjacente: "))
hipotenusa = math.hypot(c_oposto, c_adjacente)
print(hipotenusa)