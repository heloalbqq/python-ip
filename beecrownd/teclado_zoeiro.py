def substituir_letra(texto, a, b):
    resultado = ''
    for letra in texto:
        if letra == a:
            resultado += b
        elif letra == b:
            resultado += a
        else:
            resultado += letra
    return resultado

letras = []
frases = []
n, m = list(map(int, input().split()))
for _ in range(n):
    letras.append(input('').split())


for _ in range(m):
    frases.append(input(''))


for frase in frases:
    for par in letras:
        frase = substituir_letra(frase, par[0], par[1])
    print(frase)