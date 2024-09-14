def recruta_direcao():
    while True:
        N = int(input())  
        if N == 0:
            break 
        
        comandos = input().strip()  
        direcoes = ['N', 'L', 'S', 'O']  
        posicao = 0  
        
        for comando in comandos:
            if comando == 'D':
                posicao = (posicao + 1) % 4  
            elif comando == 'E':
                posicao = (posicao - 1) % 4  
        
        print(direcoes[posicao])

recruta_direcao()
