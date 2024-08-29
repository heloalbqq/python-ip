from armazem import Armazem
from moinho import Moinho
from leitor import ler_cartao
from imprimir import escrever_saida

class MaquinaAnalitica:
    def __init__(self):
        #cria instancias
        self.armazem = Armazem()
        self.moinho = Moinho()
        self.instrucoes = []
        self.instrucao_index = 0

    def configurar (self, nome_arquivo_entrada='cartao.in', nome_arquivo_saida='cartao.out'):
        #configura a maquina analitica com o arquivo de entrada e saida
        #ler_cartao(nome_arquivo_entrada) lê as instrucoes do arquivo de entrada e as armazena em self.instrucoes
        #self.nome_arquivo_saida define o nome do arquivo onde a saida sera gravada

        self.instrucoes = ler_cartao(nome_arquivo_entrada)
        self.nome_arquivo_saida = nome_arquivo_saida


    def ligar_maquina(self):

        saida = [] #armazena resultados que serao escritos na saída
        while self.instrucao_index < len(self.instrucoes):
            instrucao = self.instrucoes[self.instrucao_index]
            codigo = instrucao[:4] #4 bits da instrucao, usados para determinar a operacao a ser realizada
            
            if codigo == '0001': # STOREIM
                endereco = int(instrucao[4:8], 2) #eh extraido dos bits 4 a 7 e convertido de binsrio p decimal
                valor = int(instrucao[8:], 2) #eh extraido dos bits 8 em diante e convertido de binario p decimal
                self.armazem.armazenar (endereco, valor)

            elif codigo == '0010': # LOADOP
                endereco = int(instrucao[4:8], 2)
                valor = self.armazem.carregar (endereco)
                if self.moinho.operando1 == 0:
                   self.moinho.operando1 = valor
                else:
                    self.moinho.operando2 = valor
            
            elif codigo == '0011': # ADD
                self.moinho. adicionar()
                resultado = self.moinho.resultado
                endereco = int(instrucao[4:8], 2)
                self-armazem.armazenar (endereco, resultado) 
            
            elif codigo == '0100': # SUB
                self.moinho.subtrair()
                resultado = self.moinho.resultado
                endereco = int(instrucao[4:8], 2)
                self-armazem. armazenar (endereco, resultado) 
            
            elif codigo == '0101': # MUL
                self.moinho.multiplicar()
                resultado = self.moinho.resultado
                endereco = int(instrucao[4:8], 2)
                self.armazem.armazenar (endereco, resultado) 
            
            elif codigo == '0110': # STORE
                endereco = int(instrucao[4:8], 2) #eh extraido e convertido
                valor = self.moinho.resultado #eh o resultado armazenado no moinho
                self.armazem.armazenar (endereco, valor) 
                #o valor eh armazenado no endereco especificado na memoria
            
            elif codigo == '0111': # PRINT

                #Lê um valor da memória e o adiciona à lista de saída em formato binário

                endereco = int(instrucao[4:8], 2) #eh extraído e convertido
                valor = self.armazem.carregar (endereco) #eh carregado da memoria
                binario = format (valor, '016b') #converte o valor para uma string binaria de 16 bits
                saida.append (binario)
           
            self.instrucao_index += 1
            #avanca p a proxima instrucao na lista
        
        escrever_saida(self.nome_arquivo_saida, saida)

