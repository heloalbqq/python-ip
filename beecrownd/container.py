a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
   
if c <= z:
    um = (x // a) * (y // b) * (z // c)
    dois = (x // b) * (y // a) * (z // c)
    print(max(um, dois))
else:
    print('0')