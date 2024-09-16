#Escreva uma função recursiva produto_lista(lista) que receba uma lista de números e retorne o produto de todos os seus #elementos.

def produto(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista[0] * produto(lista[1:])
    
lista = [1, 4, 5, 2]
print(produto(lista))