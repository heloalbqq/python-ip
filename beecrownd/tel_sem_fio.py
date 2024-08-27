t = int(input())

for k in range(1, t + 1):
    frase_correta = input()
    frase_time1 = input()
    frase_time2 = input()
    
    coincidencias_time1 = 0
    coincidencias_time2 = 0
    desempate = 0 

    for i in range(len(frase_correta)):
        if frase_time1[i] == frase_correta[i]:
            coincidencias_time1 += 1
        if frase_time2[i] == frase_correta[i]:
            coincidencias_time2 += 1

        if desempate == 0:
            if frase_time1[i] == frase_correta[i] and frase_time2[i] != frase_correta[i]:
                desempate = 1
            elif frase_time2[i] == frase_correta[i] and frase_time1[i] != frase_correta[i]:
                desempate = 2
    
    print(f"Instancia {k}")
    if coincidencias_time1 > coincidencias_time2:
        print("time 1")
    elif coincidencias_time2 > coincidencias_time1:
        print("time 2")
    else:
        if desempate == 1:
            print("time 1")
        elif desempate == 2:
            print("time 2")
        else:
            print("empate")
    
    print()