'''Desenvolva um programa que leia o comprimento de tres retas e diga se elas podem ou não formarr um triangulo '''


reta1 = float(input('digite uma reta: '))
reta2 = float(input('digite a segunda medida: '))
reta3 = float(input('digite a terceira medida: '))

if reta1<reta2 + reta3 and reta2<reta1 + reta3 and reta3<reta1 +reta2:
    print('os seguimentos acima podem formar um triangulo')
else:
    print('os seguimentos nao podem formar um triangulo')

