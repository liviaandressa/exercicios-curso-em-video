#Um professor quer sorterar um dos seus alunos para apagar o quadro. Fça um programa que ajude ele, lendo o nome deles e escrevendo o nome d escolhi

import random

aluno1 = str(input("digite um nome: "))
aluno2 = str(input("digite um nome: "))
aluno3 = str(input("digite um nome: "))
#aluno4 = str(input("digite um nome: "))

lista =  [aluno1, aluno2, aluno3, ]
sorte = random.choice(lista)
print("o sorteado para pagar o certificado do curso foi você: ", sorte)
