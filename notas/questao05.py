voos = [{"numero_voo": "AA123", "cidade_origem": "São Paulo",
"horario_chegada": "10:30", "horario_partida": "11:00"},
{"numero_voo": "JJ456", "cidade_origem": "Rio de Janeiro",
"horario_chegada": "09:45", "horario_partida": "10:15"},
{"numero_voo": "BB789", "cidade_origem": "Brasília",
"horario_chegada": "08:20", "horario_partida": "08:50"},
{"numero_voo": "AA124", "cidade_origem": "São Paulo",
"horario_chegada": "14:00", "horario_partida": "14:30"},
{"numero_voo": "CC321", "cidade_origem": "Curitiba",
"horario_chegada": "12:10", "horario_partida": "12:40"}]

cidade = input('Digite a cidade de destino: ')
A = input('Digite o horário 1 (HH:MM): ') #horario_chegada1
B = input('Digite o horário 2 (HH:MM): ') #horario_chegada2

for voo in voos:
    if cidade == voo["cidade_origem"] and A <= voo["horario_chegada"] <= B:
        print(f'Numero do voo: {voo["numero_voo"]}')
        print(f'Cidade de Origem: {voo["cidade_origem"]}')
        print(f'Horario de chegada: {voo["horario_chegada"]}')
    