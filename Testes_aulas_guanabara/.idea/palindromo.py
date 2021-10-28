'''frase = str(input('digite uma frase: ')).strip().upper()
palavras_separadas = frase.split()
junto = ''.join(palavras_separadas)
inverso = ''
for x in range(len(junto) - 1, -1, -1):
    inverso += junto[x]
print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('temos um palíndromo')
else:
    print('não é um palíndromo')'''

frase = str(input('digite uma frase: ')).strip().upper()
palavras_separadas = frase.split()
junto = ''.join(palavras_separadas)
inverso = junto[:: - 1]
print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('temos um palíndromo')
else:
    print('não é um palíndromo')