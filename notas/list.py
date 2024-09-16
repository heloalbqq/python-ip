numeros = [x for x in range(10)]
print(f'Criando lista de numeros: {numeros}')


#nuneros ao quadrado
quadrado = [x**2 for x in range(10)]
print(f'Criando uma lista de quadrados: {quadrado}')

#numeros pares
pares = [x for x in range(10) if x % 2 == 0]
print(f'Criando uma lista de num pares: {pares}')

#transformando p/ maiusculas
palavras = ["Heloisa", "é", "linda"]
maiuscula = [palavra.upper() for palavra in palavras]
print(f'Deixando palavras em maiusculo: {maiuscula}')

#maiores que 5
maior_que_cinco = [x for x in numeros if x > 5]
print(f'Exibindo num maiores que 5: {maior_que_cinco}')