v1, v2, v3, v4, v5 = map(int, input().split())

if v1 < v2 < v3 < v4 < v5:
    print('C')
elif v1 > v2 > v3 > v4 > v5:
    print('D')
else:
    print('N')
