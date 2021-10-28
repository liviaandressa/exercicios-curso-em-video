# escreva um programa que converta uma temperatura e graus celsius e converta para graus fahrenheit

'''celsius = float(input("digite a temperatura em graus celsius: "))
conversao = celsius * 9 / 5 + 32
print("{}°C é igual a {}°F ".format(celsius, conversao))'''

'''f = float(input("digite a temperatura em graus Fahrenheit: "))
conversao = (f - 32) * (5 / 9)
print(" A temperatura de {}°F é equivalente a {:.2f}°C ".format(f, conversao))
'''

valor =  float(input('Informe um valor: '))
if valor > 0:
    print('O valor informado é positivo')
elif valor < 0:
    print('O valor informado é negativo')
elif valor == 0:
    print('O valor digitado é 0(zero) não se encaixa como negativo ou positivo.')