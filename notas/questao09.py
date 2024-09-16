#Escreva uma função recursiva soma_elementos_pares(lista) que receba uma lista de números e retorne a soma de todos os elementos que são pares.

def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] % 2 == 0:
            return lista[0] + soma(lista[1:]) 
        else:
            return soma(lista[1:])

lista = [1, 2, 3, 4]
print(soma(lista))

