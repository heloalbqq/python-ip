'''
Questão 02
Implemente o jogo da adivinhação. Neste jogo, um número é sorteado e o usuário
tenta adivinhar esse número por meio de uma sequência de palpites, ao passo que
vai recebendo feedbacks indicando se o número alvo é "maior" ou "menor" que o
último palpite dado. Para sortear um número inteiro, podemos usar a função
randint do módulo random.
'''

import random

numero = random.randint(1,13)
print(numero)
resposta = input("Digite um número: ")
resposta = int(resposta)

if numero > resposta:
    print("resposta MENOR que o numero")
elif numero < resposta: 
        print("resposta MAIOR que o numero")
else: 
        print("resposta correta")        