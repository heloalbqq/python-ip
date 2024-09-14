def processar_instrucoes():
    T = int(input()) 
    
    for _ in range(T):
        n = int(input()) 
        instrucoes = []  
        posicao = 0 
        
        for _ in range(n):
            comando = input().strip()
            
            if comando == "LEFT":
                instrucoes.append(-1)  
                posicao -= 1  
            elif comando == "RIGHT":
                instrucoes.append(1)
                posicao += 1  
            else:
                _, _, i_str = comando.split() 
                i = int(i_str) - 1  
                movimento = instrucoes[i]  
                instrucoes.append(movimento)  
                posicao += movimento  

        print(posicao)

processar_instrucoes()
