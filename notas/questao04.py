"""
Escreva uma função recursiva soma_chave(lista, chave) que receba uma lista
de dicionários e uma chave específica, e retorne a soma dos valores associados a
essa chave em todos os dicionários da lista.
dados = [
{"nome": "Alice", "idade": 25, "salario": 3000},
{"nome": "Bob", "idade": 30, "salario": 4000},
{"nome": "Carlos", "idade": 35, "salario": 5000}
]
soma_chave(dados, "salario") # Retorna 12000

"""

def soma_chave(lista, chave):
    if len(lista) == 0:
        return 0
    else:
        valor = lista[0].get(chave, 0)
        return valor + soma_chave(lista[1:], chave)
    
dados = [
{"nome": "Alice", "idade": 25, "salario": 3000},
{"nome": "Bob", "idade": 30, "salario": 4000},
{"nome": "Carlos", "idade": 35, "salario": 5000}
]

print(soma_chave(dados, "salario"))