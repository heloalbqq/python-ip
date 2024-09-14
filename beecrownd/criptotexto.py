def extrair_maiusculas(mensagem):
    return ''.join([char for char in mensagem if char.isupper()])

def main():
    import sys
    input = sys.stdin.read
    dados = input().splitlines()
    
    C = int(dados[0])
    
    resultados = []
    for i in range(1, C + 1):
        mensagem = dados[i]
        resultado = extrair_maiusculas(mensagem)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
