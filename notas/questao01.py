#Escreva uma função recursiva soma_lista(lista) que receba uma lista de
#números e retorne a soma de todos os seus elementos.

def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
    
lista = [1, 2, 3, 4]
print(soma_lista(lista))