'''
Escreva um programa em Python que leia uma sequência de DNA e encontre o seu
reverso complementar. O reverso complementar é formado substituindo cada
nucleotídeo pelo seu complementar (A ↔ T, C ↔ G) e, em seguida, invertendo a
sequência.
'''

import re

sequencia = input("Digite a seguencia de DNA: ")

seq= sequencia.upper()

print(seq)

substituicoes = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

nova_seq = ''.join(substituicoes.get(char,char) for char in seq)

invertida = nova_seq[::-1]

print(nova_seq)
