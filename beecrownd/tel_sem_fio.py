instancias = int(input())


for i in range(instancias):
    instancias_num = i + 1

    verdadeiro = input()
    time1 = input()
    time2 = input()

    conjunto1 = set()
    conjunto2= set()
    conjunto3 = set()

    for letra in verdadeiro:
        conjunto1.add(letra)

    for letra in time1:
        conjunto2.add(letra)

    for letra in time2:
        conjunto3.add(letra)

    comuns1 = conjunto1 & conjunto2
    comuns2 = conjunto1 & conjunto3

    tam_comuns1 = len(comuns1)
    tam_comuns2 = len(comuns2)

    print(f'Instancia {instancias_num}')

    if tam_comuns1 > tam_comuns2:
        print('time 1')
    elif tam_comuns1 == tam_comuns2:
        print('empate')
    else: 
        print('time 2')