#Dado três números inteiros a, b, e c, escreva um programa em C ou Python que prove que, se a divide b (a|b) e b divide c (b|c), então a também divide c (a|c)..

for a in range(1, 6):
    for b in range(1, 6):
        for c in range(1, 6):

            if b % a == 0 and c % b == 0:
                if c % a == 0:
                    print(f'para a = {a}, b = {b} e c = {c}: a divide b e b divide c, entao a divide c')
                else: 
                    print(f'para a = {a}, b = {b} e c = {c}: a divide b e b divide c, entao a nao divide c(o que nao deve acontecer)')