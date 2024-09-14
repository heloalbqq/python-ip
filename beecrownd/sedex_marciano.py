import math

def cabe(L, A, P, R):
    diagonal_caixa = math.sqrt(L**2 + A**2 + P**2)

    diametro = 2 * R

    if diagonal_caixa <= diametro:
        return 'S'
    else:
        return 'N'

L, A, P, R = map(int, input().split())

print(cabe(L, A, P, R))
