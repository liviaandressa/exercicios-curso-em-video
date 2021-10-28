soma = 0
for c in range(0,6):
    valor = int(input('digite um numero: '))
    if valor %2 == 0:
        soma += valor
print('a soma é: ', soma)