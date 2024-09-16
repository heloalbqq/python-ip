#Escreva uma função recursiva encontrar_maximo(lista) que receba uma lista de números e retorne o maior valor presente na lista.

#lista = [1, 2 ,3, 5, 4]
#print(max(lista))

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_num = maximo(lista[1:])
        return max(lista)
    
lista = [1, 3, 6, 8 , 3]
print(maximo(lista))