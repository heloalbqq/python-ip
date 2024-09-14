N = int(input().strip())

menor_preco = float('inf')

for _ in range(N):

    preco, peso = input().strip().split()
    preco = float(preco)
    peso = int(peso)

    preco_por_kg = (preco * 1000) / peso
   
    if preco_por_kg < menor_preco:
        menor_preco = preco_por_kg
print(f"{menor_preco:.2f}")
