#Faça um programa para sortear a ordem de apresentação de trebalhso dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1= str(input("digite um nome: "))
aluno2= str(input("digite um nome: "))
aluno3= str(input("digite um nome: "))
aluno4= str(input("digite um nome: "))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(lista)