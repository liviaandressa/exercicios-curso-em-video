#faça um programa que leia um número entre 0 a 9999 e mostre ca um dos seus digitos separados

numero =  int(input('digite um número entre 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena =  numero // 100 % 10
milhar = numero // 1000 % 10
print("analisando o numero {}. vimos que ele tem:".format(numero))
print("unidade: {}".format(unidade))
print("dezena: {} ".format(dezena))
print("centena: {}".format(centena))
print("milhar: {} ".format(milhar))
