class Moinho:
    
    def init_(self):
        self.operando1 = 0
        self.operando2 = 0
        self.resultado = 0

    def carregar_operandos(self, valor1, valor2):
        self.operando1 = valor1
        self.operando2 = valor2

    def adicionar(self):
        self.resultado = self.operando1 + self.operando2

    def subtrair(self):
        self.resultado = self.operando1 - self.operando2

    def multiplicar(self):
        self.resultado = self.operando1 * self.operando2