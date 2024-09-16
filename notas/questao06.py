from datetime import datetime

preco = {"uma_bola": 2.00, "duas_bolas": 4.00}

vendas = []

while True:
    tipo = input('Qual o tipo de sorvete (uma_bola ou duas_bolas)? ')
    if tipo not in preco:
        print("Tipo de sorvete inválido!")
        continue
    quantidade = int(input('Quantidade: '))
    data_venda = datetime.now().strftime("%Y-%m-%d")  # Formato YYYY-MM-DD

    venda = {
        "tipo_sorvete": tipo,
        "quantidade": quantidade,
        "data_venda": data_venda,
        "preco": preco[tipo]
    }

    vendas.append(venda)
    resposta = input('Deseja registrar outra venda? (s: sim, n: não): ')

    if resposta == 'n':
        break    

data = input('Digite a data para o relatório (YYYY-MM-DD): ')
tot_vendas = 0
tot_quantidade = 0
tot_valor = 0

for venda in vendas:
    if venda["data_venda"] == data:
        tot_vendas += 1
        tot_quantidade += venda["quantidade"]
        tot_valor += venda["quantidade"] * venda["preco"]

print(f"\nRelatório para {data}:")
print(f"Total de vendas: {tot_vendas}")
print(f"Quantidade total de sorvetes vendidos: {tot_quantidade}")
print(f"Valor total arrecadado: R${tot_valor:.2f}")

