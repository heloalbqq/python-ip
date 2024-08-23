n = int(input())

for _ in range(n):
    str1, str2 = input().split()
    resultado = ""

    for i in range(min(len(str1), len(str2))):
        resultado += str1[i] + str2[i]

    if len(str1) > len(str2):
        resultado += str1[len(str2):]
    else: 
        resultado += str2[len(str1):]

    print(resultado)