'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

reta1 = float(input('digite uma reta: '))
reta2 = float(input('digite a segunda medida: '))
reta3 = float(input('digite a terceira medida: '))

if reta1<reta2 + reta3 and reta2<reta1 + reta3 and reta3<reta1 +reta2:
    print('pode formar um triangulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não pode formar um trângulo')