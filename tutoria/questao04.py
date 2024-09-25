'''
Suponha que A, B e C representam condições que serão
verdadeiras e falsas quando um programa é executado. Suponha
ainda que desejamos que este programa realize alguma tarefa
somente quando A ou B forem verdadeiras (mas não ambas) e C
for falsa.
a) Usando A, B e C e os conectivos E, OU e NOT, escreva uma
sentença que será verdadeira apenas nestas condições.
b) Usando A, B e C e os conectivos E, OU e NOT, escreva uma
sentença que será falsa apenas nestas condições.
'''

def verd(A, B, C):
    return (A != B) and not C

def false(A, B, C):
    return not ((A != B) and not C)

# lembrar que C eh false
condicoes = [(True, True, False), (True, False, False), (False, True, False), (False, False, False)]

for A, B, C in condicoes:
    print(f"{A}, {B}, {C} = {verd(A, B, C)}, {false(A, B, C)}")

    #aa