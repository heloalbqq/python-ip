#Escreva um programa em C ou Python que comprove que, se o quadrado de um número for ímpar, então o número original também é ímpar.

for num in range(-3, 4):
    quadrado = num ** 2

    if quadrado % 2 == 0:
        print(f'{num} eh impar, pois seu quadrado {quadrado} tb eh impar')
    else:
        print(f'{num} eh impar, pois seu quadrado {quadrado} tb eh impar(o que esta errado)')
