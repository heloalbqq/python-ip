#Implemente um programa em C ou Python que demonstre que o produto de dois números inteiros pares sempre resulta em um número par.

for x in range(-3, 4):
    for y in range(-3, 4):

        if x % 2 == 0 and y % 2 == 0:
            produto = x * y

            if produto % 2 == 0:
                print(f'o produto de {x} e {y} é = {produto}, que eh par')
            else:
                print(f'o produto de {x} e {y} é = {produto}, que eh impar(o que esta errado)')