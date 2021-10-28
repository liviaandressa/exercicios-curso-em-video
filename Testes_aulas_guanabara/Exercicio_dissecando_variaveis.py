# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

nome = input("digite alguma coisa: ")
print("O tipo primitivo desse valor é: ", type(nome))
print("é numérico?", nome.isnumeric())
print("é somente espaços?", nome.isspace())
print("é alfabético?", nome.isalpha())
print("tem letras e números?", nome.isalnum())
print("as letras são minúsculas ?", nome.islower())