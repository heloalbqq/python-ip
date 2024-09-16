#Escreva uma função recursiva soma_pares_chave(lista, chave) que receba uma lista de dicionários e uma chave específica, e retorne a soma dos valores associados a essa chave, mas somente se os valores forem pares.

def soma(lista, chave):
    if len(lista) == 0:
        return 0
    else:
        valor = lista[0].get(chave, 0)
        return valor + soma(lista[1:], chave)
    
dados = [
    {'idade': 13, 'salario': 200.00},
    {'idade': 20, 'salario': 2500.00},
    {'idade': 24, 'salario': 6470.00},
    {'idade': 19, 'salario': 1330.00},
]

print(soma(dados, 'salario'))