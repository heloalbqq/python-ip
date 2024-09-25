'''
Escreva um algoritmo que leia dois valores numéricos e depois
mostre o MDC e MMC entre eles. justifique a lógica utilizada, esse
algoritmo funciona para todos os casos ? Como podemos verificar
essa comprovação para todos os casos de testes possíveis?
'''
import math

def mdc(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def mmc(x, y):
    return abs(x * y) // mdc(x, y)

num1, num2 = map(int, input().split())

max_divisor = mdc(num1, num2)
min_multiplo = mmc(num1, num2)

print(f'MDC = {max_divisor}')
print(f'MMC = {min_multiplo}')


'''
Existem dois valores: "x" e "y", onde x > y. o cpodigo substitui x por y e y pelo resto de x e y. Isso se repete, com a condicao while, até que y = 0, entao o valor de x é o MDC. E para calcular o MMC, existe uma formula: MMC = (x * y)/mdc(x e y)

Os testes possiveis sao para todos os numeros inteiros > 0 e pares
'''