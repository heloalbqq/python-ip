def calcular_max_containers(A, B, C, X, Y, Z):
    max_containers = 0
 
    orientacoes = [
        (A, B, C),
        (A, C, B),
        (B, A, C),
        (B, C, A),
        (C, A, B),
        (C, B, A)
    ]

    for largura, comprimento, altura in orientacoes:
        if altura <= Z:
            num_largura = X // largura
            num_comprimento = Y // comprimento
            num_altura = Z // altura

            containers = num_largura * num_comprimento * num_altura

            max_containers = max(max_containers, containers)
    
    return max_containers

A, B, C = map(int, input().strip().split())
X, Y, Z = map(int, input().strip().split())

print(calcular_max_containers(A, B, C, X, Y, Z))
