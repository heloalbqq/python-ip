'''
Dados os valores lógicos A é verdadeiro, B é falsa e C é
verdadeira.Qual o valor lógico de cada expressão a seguir?
a) A ^(B v C)
b) (A ^B) v C
c) (A ^B)’ v C
d) A’ V (B’ ^C)
Seguindo a lógica computacional, como poderia ser resolvido esse
problema em forma de um algoritmo funcional? se possível, mostre uma
implementação.
'''

A = True
B = False
C = True

print(f'A ^ (B v C) = {A and (B or C)}')
print(f'(A ^ B) v C = {(A and B) or C}')
print(f'(A ^ B)’ v C = {not (A and B) or C}')
print(f'A’ V (B’ ^C) = {not A or (not B and C)}')

