'''
Se o usuário digita a letra "O" ou "o", assumimos que ele queria digitar o número "0".

2. Se o usuário digita a letra "l", assumimos que ele queria digitar o número "1".

3. Vírgulas e espaços são permitidos, porém não são processados (são ignorados).

Se, mesmo com as regras acima, o usuário não entrou um número não-negativo, imprima a string "error". Overflow (um valor maior que 2147483647) é considerado inválido e "error" deve ser impresso.
'''
while True: 
    try:
        
        n = input()

        n = (n.replace('o', '0').replace('O', '0').replace('l', '1').replace(',', '').replace(' ', ''))

        if n and n.isdigit():
            num = int(n) 
            if num <= 2147483647:
                print(num)
            else:
                print("error")  
        else:
            print("error") 
    except EOFError:
        break






