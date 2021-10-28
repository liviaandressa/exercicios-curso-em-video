'''escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuáro tentar descobrir qua foi o número escolhido pelo computador.
o programa deverá escrever na tela se o usuário venceu ou perdeu'''

'''
1° solução 

import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
numero = int(input('Em que número que  pensei?  '))
lista = [0, 1, 2, 3, 4, 5]
sortear =  random.choice(lista)
if numero == sortear:
    print("Parabéns! {} foi o número que eu pensei.".format(sortear))
else:
    print('Você errou! o número que eu pensei foi o número {}'.format(sortear))'''

#Segunda solução

from random import randint
from time import sleep
def linhas():
    print('***' * 20)

computador  = randint(0, 5)
linhas()
print('Vou pensar entre um número entre 0 e 5. Tente adivinhar...')
linhas()
jogador = int(input("Em que número eu pensei? "))
print('processando...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))
