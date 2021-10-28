'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

from datetime import date
ano =  int(input("Qual ano você quer analisar? Digite 0(zero) para verificar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # a cada quatro anos, exceto em multiplos de 100 que são multiplos de 400
    print("O ano {} é BISSEXTO".format(ano))
else:
    print('O ano {} NÃO É BISSEXTO! '.format(ano))
