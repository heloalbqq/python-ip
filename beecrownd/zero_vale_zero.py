def remove_zeros(num):
    return int(''.join(d for d in str(num) if d != '0'))

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    soma = m + n
    resultado_sem_zero = remove_zeros(soma)
    
    print(resultado_sem_zero)