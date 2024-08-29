def ler_cartao(nome_arquivo):
    with open (nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    instrucoes = []
    for linha in linhas:
        linha = linha.strip()
        if len(linha) == 16:
            binario = ''.join('1' if c == 'X' else '@' for c in linha)
            instrucoes.append (binario)
    return instrucoes


# o arquivo eh aberto e lido linha por linha
# cada linha eh verificada para garantir que tem 16 caracteres
# os caracteres X sao convertidos em 1 e O em 0, gerando uma string binaria de 16 bits
# as strings binarias sao adicionadas a uma lista e retornadas