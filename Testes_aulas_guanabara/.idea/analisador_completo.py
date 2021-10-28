soma = 0
maior_idade= 0
mais_velho = ''
mulher20 = 0
for p in range(1, 5):
    print(f'----------{p}ª PESSOA ----------')
    nome=  str(input('Digite o nome: '))
    idade = int(input('digite sua idade: '))
    sexo = str(input('informe o sexo [F/M]: ')).upper()
    soma += idade

    if p == 1 and sexo == 'M':
        maior_idade = idade
        maior_idade = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1

print(f'A média da idade desse grupo é de: {soma / p}')
print(f'O homem mais velho tem  {maior_idade} e se chama {mais_velho}')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos')



