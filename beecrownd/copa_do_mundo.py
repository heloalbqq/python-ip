def determinar_campeao():
    equipes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    
    vencedores = []

    for i in range(8):
        M, N = map(int, input().split())  
        if M > N:
            vencedores.append(equipes[2 * i])  
        else:
            vencedores.append(equipes[2 * i + 1]) 

    quartas = []
    for i in range(4):
        M, N = map(int, input().split())
        if M > N:
            quartas.append(vencedores[2 * i]) 
        else:
            quartas.append(vencedores[2 * i + 1]) 

    semi = []
    for i in range(2):
        M, N = map(int, input().split())
        if M > N:
            semi.append(quartas[2 * i])  
        else:
            semi.append(quartas[2 * i + 1]) 

    M, N = map(int, input().split())
    if M > N:
        campeao = semi[0] 
    else:
        campeao = semi[1]  

    print(campeao)

determinar_campeao()
