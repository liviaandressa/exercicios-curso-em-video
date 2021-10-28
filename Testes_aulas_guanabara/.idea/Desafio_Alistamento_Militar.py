'''Faça um programa
que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

'''
nascimento = int(input('Informe o seu ano de nascimento'))
data = 2021
alistamento = data - nascimento
if alistamento < 18:
    print('você ainda vai se alistar no serviço militar')
elif alistamento == 18:
    print('Está na hora exata de você se alistar')
elif alistamento > 18:
    print('Já pssou da hora de você e alistar')
'''

#Resolção Gauanabara

from datetime import date
ano_atual = date.today().year
nascimento =  int(input('Informe o ano que você nasceu: '))
idade = ano_atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano_atual))
if idade == 18:
    print('Você tem que se alista imediatmente!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não em 18 anos. Falta {} para você se alistar.'.format(saldo))
elif idade > 18:
    saldo =  idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
