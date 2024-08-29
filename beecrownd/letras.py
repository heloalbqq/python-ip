letra = input().strip()
frase = input().strip()
palavras = frase.split()

num_palavras = len(palavras)

contador = sum(letra in palavra for palavra in palavras)

#quant de palavras com a letra * 100 / tot de palavras
if num_palavras > 0:
    porcentagem = (contador * 100) / num_palavras
else:
    porcentagem = 0.0

print(f'{porcentagem:.1f}')