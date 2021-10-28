'''Escreva um programa que leia u número inteiro qualquer e peça para o usuário escolher qal será a base de conversão:
1 para binário
2 para octal e
3 para hexadecimal'''

numero =  int(input('Digite um número inteiro: '))
conversão = int(input('''Ecolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
Sua opção: '''))
if conversão == 1:
    print('{} convertido para BINÁRIO é igual  a {}'.format(numero, bin(numero) [2:]))
elif conversão == 2:
    print('{} convertido para OCTAL é igual  a {}'.format(numero, oct(numero) [2:]))
else:
    print('{} convertido para HEXADECIMAL é igual  a {}'.format(numero, hex(numero) [2:]))