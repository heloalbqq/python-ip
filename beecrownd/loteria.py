def verificao():
    aposta = set(map(int, input().split()))  
    sorteio = set(map(int, input().split())) 
    
    acertos = len(aposta & sorteio)

    if acertos == 6:
        print("sena")
    elif acertos == 5:
        print("quina")
    elif acertos == 4:
        print("quadra")
    elif acertos == 3:
        print("terno")
    else:
        print("azar")

verificao()
