import banco
import random


print("Bem-vindo ao Banco do Silvio Santos\n")

opt = 0
while opt != 6:
    print("Escolha uma opcao do menu:")
    print("1 - Cadastrar cliente")
    print("2 - Visualizar cadastros")
    print("3 - Deposito")
    print("4 - Saque")
    print("5 - PIX")
    print("6 - Sair")
    opt = int(input())

    if opt == 1:
        nome = input("Digite o nome do cliente: ")
        numero = random.randint(1000,9999)
        banco.cadastrar_conta(nome,numero)
    elif opt == 2:
        ret = banco.consultar_contas()
        for elemento in ret:
            print(f"Cliente: {elemento[0]} | NoConta: {elemento[1]}")
    elif opt == 3:
        conta = int(input("Digite o numero da conta: "))
        valor = float(input("Digite o valor depositado: "))
        ret = banco.credito(conta, valor)
        if ret == 0:
            print("Deposito realizado com sucesso")
        else:
            print("Lamento! Mas a conta não existe.")
    elif opt == 4:
        conta = int(input("Digite o numero da conta: "))
        valor = float(input("Digite o valor a ser sacado: "))
        ret = banco.debito(conta, valor)
        if ret == 0:
            print("Dinheiro esta em sua mao!")
        elif ret == -1:
            print("Esta conta não foi identificada.")
        else:
            print("Quer um emprestimo?")
    elif opt == 5:
        origem = int(input("Digite o numero da conta origem: "))
        destino = int(input("Digite o numero da conta destino: "))
        valor = float(input("Digite o valor do PIX:"))
        ret = banco.pix(origem, destino, valor)
        if ret == -3:
            print("Infelizmente, algo deu errado na conta origem.")
        elif ret == -4:
            print("Pix ping-pong!")
        else:
            print("O dinheiro já tá lá, pai")