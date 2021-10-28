'''Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando  R$0,50  por Km para viagen s de até 200Km  e R$0,45 para viagens mais longas'''



distancia =  float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começau ma viagem de {}Km'.format(distancia))
if distancia <= 200:
    passagem = distancia * 0.50
    print('A sua passagem irá custar R$ {}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('A sua passagem irá custar R${}'.format(passagem))