
def converter_frases(n, m, trocas, frases):
    mapeamento = {}
    for troca in trocas:
        original, substituto = troca
        mapeamento[original] = substituto

    frases_convertidas = []
    for frase in frases:
        frase_convertida = ''.join(mapeamento.get(char, char) for char in frase)
        frases_convertidas.append(frase_convertida)

    return frases_convertidas

def processar_entrada():
    import sys
    input = sys.stdin.read
    dados = input().strip().split('\n')
    
    n, m = map(int, dados[0].split())
    
    trocas = [tuple(linha.split()) for linha in dados[1:n+1]]
    
    frases = dados[n+1:n+1+m]
    
    frases_convertidas = converter_frases(n, m, trocas, frases)
    for frase in frases_convertidas:
        print(frase)
        
if __name__ == "__main__":
    processar_entrada()
