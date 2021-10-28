sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]

while sexo not in 'FM':
    sexo = str(input('Por favor, informe um valor válido: ')).strip().upper()[0]

print(f'Sexo {sexo} validado')

