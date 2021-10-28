from random import randint

print('Eu sou o computador... ')
print('Acabei de pensar em um número nentre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
print('-' * 50)
jogador = int(input('Tente adivinhar o número que eu pensei: '))

computador = randint(0, 10)
contador = 1

while jogador != computador:
    if jogador > computador:
        jogador = int(input('MENOS. Tente mais uma vez: '))
    else:
        jogador = int(input('MAIS. Tente mais uma vez: '))
    contador += 1

print(f'Você acertou! eu pensei no número {computador}')
print(f'Você jogou {contador} para poder acertar o número')