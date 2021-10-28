#faça um programa que leia o noe completo de uma pessoa, mostrando em seguida o peimeiro e eo ltimo nome separada mente

nome = str(input('digite o seu nome compeleto: ')).strip()
contar = nome.split()
print('muito prazer em te conhecer')
print('seu primeiro nome é {}'.format(contar[0]))
print('seu ultimo nome é {}'.format(contar[len(contar)-1]))