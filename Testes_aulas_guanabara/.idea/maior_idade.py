
maior = 0
menor = 0
for i in range(1,8):
    data = int(input('Infrme a tara de nascimento: '))
    if 2021 - data >= 18:
        maior +=1
    else:
        menor +=1

print(f'{maior} pessoas já são maiores de idade e {menor} pessoas ainda são menores de idade')

