#faça im programa que leia o nomde de uma pessoa e diga se ela tem Silva no nome


nome =  str(input("digite o seu nome completo: "))
verificar = nome.lower()
print(" no seu nome existe a palavra silva? ", 'silva' in verificar)
