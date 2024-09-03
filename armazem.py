class Armazem:
    def __init__(self):
        self.memoria = [0] * 16

    def armazenar (self, endereco, valor):
        self.memoria[endereco] = valor
        
       


    def carregar (self, endereco):
        return self.memoria[endereco]
    
    #endereco: O índice da lista de onde o valor deve ser lido. É um número inteiro que representa o endereço de memória
    #retorna o valor armazenado na posicao da lista self.memoria no indice endereco
    #permite ler dados da memoria da maquina a partir de um endereco especifico
