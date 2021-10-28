#escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

metros =  float(input("digite os metros: "))
centimetros = metros*100
milimetros = metros*1000
quilo = metros * 0.001

print("{} metros é equivalente a {} centimetros e {} milimetros".format(metros, centimetros, milimetros))
print("quilometros: {}".format(quilo))