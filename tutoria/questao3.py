# Escreva um programa em C ou Python que comprove que a soma de dois números inteiros pares sempre resulta em um número par.

for x in range(-3, 4):
    for y in range(-3, 4):

        if x % 2 == 0 and y % 2 == 0:
            soma = x + y

            if soma % 2 == 0:
                print(f'os valores {x} e {y} somados é = {soma}. Logo, eh um numero par')
            else:
                print(f'os valores {x} e {y} somados é = {soma}. Logo, eh um numero ímpar(o que esta errado)')