# Implemente um programa em C ou Python que demonstra que a soma de um número inteiro par com um número inteiro ímpar sempre resulta em um número ímpar.

for x in range(-3, 4):
    for y in range(-3, 4):

        if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
            soma = x + y

            if soma % 2 != 0:
                print(f'a soma do num par {x} e do numero impar {y} resulta em um numero impar = {soma}')
            else:
                print(f'a soma do num par {x} e do numero impar {y} resulta em um numero par = {soma}(o que esta errado)')