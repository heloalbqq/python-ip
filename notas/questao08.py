#Escreva uma função recursiva invertir_lista(lista) que receba uma lista e retorne a lista invertida.

def inverter(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + inverter(lista[:-1])
    
dados = [1, 2, 3, 4]
print(inverter(dados))