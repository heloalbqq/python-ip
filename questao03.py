'''
Faça um algoritmo que implemente a tabela verdade de um
conectivo lógico(conjunção , disjunção , condicional ,
bicondicional e ou exclusivo). ,
'''

def tab_verd():
    print(f"{'A':<5} {'B':<5} {'A AND B':<10} {'A OR B':<10} {'A IMPLIES B':<15} {'A IFF B':<10} {'A XOR B':<10}")
    
    for A in [True, False]:
        for B in [True, False]:

            e_ab = A and B
            ou_ab = A or B
            implica_ab = not A or B
            sse_ab = A == B
            exclusivo_ab = A != B
            
            print(f"{A:<5} {B:<5} {e_ab:<10} {ou_ab:<10} {implica_ab:<15} {sse_ab:<10} {exclusivo_ab:<10}")

tab_verd()

# 1 eh verdadeiro
# 2 eh falso
