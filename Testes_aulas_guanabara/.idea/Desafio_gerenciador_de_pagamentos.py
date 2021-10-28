


preço_compras = float(input('preço das compras: '))
print("[1] - à vista dinheiro\n"
        "[2] – à vista no cartão\n"
        "[3] - em até 2x no cartão \n"
        "[4] - 3x ou mais no cartão: 20% de juros")

opçao = int(input('qual é a forma de pagamento: '))

#
if opçao == 1:
    total = preço_compras - (preço_compras * 10 / 100)

elif opçao == 2:
    total = preço_compras - (preço_compras * 5 / 100)
elif opçao == 3:
    total = preço_compras
    parcela = total / 2
    print('sua compra será parcelada em 2x de {} sem juros '.format(parcela))
elif opçao == 4:
    total = preço_compras + (preço_compras * 20 / 100)
    total_parcelas = int(input("Em quantas parcelas: "))
    parcela = total / total_parcelas
    print('suas compras seram parceladas em {}x de {} com juros'.format(total_parcelas, parcela))
print('sua compra vai custar {} no final'.format(total))