n = int(input().strip())

pokemons = set()
for _ in range(n):
    pokemons.add(input().strip())

tot_pokemons = 151

faltam = tot_pokemons - len(pokemons)

print(f'Falta(m) {faltam} pokemon(s)')
