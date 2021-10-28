#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas
#o nome com todas minúsculas
#quantas letras ao todo sem considerar espaços
#quantas letras tem o prmeiro nome


nome = str(input('digite o seu nome: ')).strip() #já elimina s espaços antes e depois
print('o seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('o seu nome em letras minúsculas é: {}'.format(nome.lower()))
print(' o seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))
#print('o seu primeiro nome tem: {} letras'.format(nome.find(' ')))
primeiro_nome = nome.split() #jeito que eu queria fazer mas n~~ão sabia como
print('seu primeio nome é {} e ele tem {}  letras'.format(primeiro_nome[0], len(primeiro_nome[0])))





