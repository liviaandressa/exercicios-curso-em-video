'''Escreve um programa que leia a vlocidade de um carro. Se ele ultrapassar 80km/h, motre uma mensagem dizendo que ele foi multado. A mlya vai custar R$7,00 por cada Km acima do limite'''

velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia e dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia e dirija com segurança!')