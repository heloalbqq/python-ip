#Escreva uma função recursiva lista_ordenada(lista) que receba uma lista de
#números e retorne True se a lista estiver ordenada em ordem crescente, e False
#caso contrário.

def lista_ordenada(lista):
    if len(lista) <= 1:
        return True
    if lista[0] > lista[1]:
        return False

    return lista_ordenada(lista[1:])
        
        
lista = [1, 9, 3, 4]
print(lista_ordenada(lista))