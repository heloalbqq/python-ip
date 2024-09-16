registros = []

def cadastrar_conta(nome, numero, saldo=0.0):
    if not existe_conta(numero):
        registros.append({'cliente': nome, 'no-conta': numero, 'saldo': saldo})
        return 0
    else:
        return -5

def consultar_contas():
    return [(dic_conta['cliente'], dic_conta['no-conta']) for dic_conta in registros]

def existe_conta(numero):
    for conta in registros:
        if conta['no-conta'] == numero:
            return True
    return False

def debito(numero, valor):
    if existe_conta(numero):
        for conta in registros:
            if conta['no-conta'] == numero:
                if conta['saldo'] >= valor:
                    conta['saldo'] = conta['saldo'] - valor
                    return 0
                else:
                    return -2
    else:
        return -1

def credito(numero, valor):
    if existe_conta(numero):
        for conta in registros:
            if conta['no-conta'] == numero:
                conta['saldo'] = conta['saldo']+valor
                return 0
    else:
        return -1
        

def pix(conta_origem, conta_destino, valor):

    ret_origem = debito(conta_origem, valor)
    if ret_origem == 0:
        ret_destino = credito(conta_destino, valor)
        if ret_destino != 0:
            credito(conta_origem, valor)
            return -4
        return 0
    else:
        return -3
