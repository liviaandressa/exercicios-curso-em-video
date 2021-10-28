from random import randint

tupla_intens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print(''' Suas opções: 
0 - pedra
1 - papel 
2 - tesoura''')
jogador = input('informe a opção que você deseja escolher: ')

print('o computador escolheu {}'.format(tupla_intens[computador]))

if jogador == computador: #empate
    print("empatou")

#papel enrola pedra
elif jogador == 1 and computador == 0: #computador
    print('computador ganhou')
elif computador == 0 and jogador == 1: #jogador
    print('jogador ganhou')

#pedra quebra tesoura
elif jogador == 0 and computador == 2: #jogador
    print('jogador ganhu')
elif computador == 2 and jogador == 0: #computador
    print('computador ganhou')

#tesoura corta papel
elif jogador == 2 and computador == 1: #jogador
    print('jogador ganhu')
elif computador == 1 and jogador == 2: #computador
    print('computador ganhou')
else:
    print('opção inválida')






