'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
ano_atual = date.today().year
ano = int(input('Informe seu ano de nascimento: '))
classificao = ano_atual - ano
print('você tem {} anos de idade '.format(classificao))
if classificao <= 9:
    print('MIRIM')
elif  classificao > 9 and classificao <= 14:
    print('INFANTIL')
elif classificao > 14 and classificao <= 19:
    print('JÚNIOR')
elif classificao > 19 and classificao <= 25:
    print('SÊNIOR')
elif classificao > 25:
    print('MASTER')