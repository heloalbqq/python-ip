#Escreva uma função recursiva contar_ocorrencias(lista, elemento) que
#receba uma lista e um elemento, e retorne o número de vezes que o elemento
#aparece na lista.

def contar_ocorrencias(lista, elemento):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] == elemento:
            return 1 + contar_ocorrencias(lista[1:], elemento)
        else:
            return contar_ocorrencias(lista[1:], elemento)
        
dados = [2, 4, 2, 5 , 21, 2]
print(contar_ocorrencias(dados, 5))