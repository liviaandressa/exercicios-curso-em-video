numero =  int(input('digite um número: '))
contador = 0
for i in range(1,numero + 1,1):
    if numero % i ==0:
        print('\033[34m', end='')
        contador +=1
    else:
        print('\033[35m', end='')
    print(i, end=' ')
    
print(f'\n\033[mO numero {numero} foi dividido {contador} vezes')
if contador == 2:
    print('E por isso eé é primo')
else:
    print('E por sso ele não é primo')
