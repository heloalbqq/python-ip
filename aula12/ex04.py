import re

numero = input("Digite seu número: ")

numero = re.sub(r'\D', '', numero)

if len(numero) < 10 or len(numero) > 11:
    print("Número inválido")
else:

    if len(numero) == 11:
        ddd = numero[:2] 
        telefone = numero[2:] 
    elif len(numero) == 10:
        ddd = numero[:2] 
        telefone = '9' + numero[2:]  
    else:
        print("Número inválido")
        exit()

    if len(telefone) != 8 and len(telefone) != 9:
        print("Número inválido")
    else:
        telefone_formatado = f"({ddd}) {telefone[:5]}-{telefone[5:]}"
        print(telefone_formatado)
