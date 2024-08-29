def escrever_saida(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        for dado in dados:
            linha = ''.join('X' if bit == '1' else 'O' for bit in dado)
            arquivo.write(linha + '\n')