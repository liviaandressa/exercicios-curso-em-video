#FAÇA UM PROGRAMA QUE LEIA UMA FRASE E MOTRE QUANTAS VEZES APARECE A LETRA 'A', EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ E A ULTIMA VEZ


frase =  str(input("digite uma frase: ")).lower().strip()
print('aletra A apareceu {} vezes '.format(frase.count('a')))
print("a letra A aparece pela primeira vez na posição {}".format(frase.find('a') +1))
print('a letra A aparece pela ultima vez na posição {}'.format(frase.rfind('a') +1))
