#Escreva um programa em C ou Python que comprove que o produto de dois números inteiros ímpares sempre resulta em um número ímpar.

for x in range(-3, 4):
    for y in range(-3, 4):

        if x % 2 != 0 and y % 2 != 0:
            produto = x * y 

            if produto % 2 != 0:
                print(f'o produto dos numeros {x} e {y} é = {produto}. Logo, eh um numero impar')
            else:
                print(f'o produto dos numeros {x} e {y} é = {produto}. Logo, eh um numero par(o que esta errado)')