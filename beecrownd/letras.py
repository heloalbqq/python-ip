letra = input()
frase = input()
palavras = frase.split()

for palavra in palavras:
    if letra in palavra:
        print('ok')
    else:
        print('fail')