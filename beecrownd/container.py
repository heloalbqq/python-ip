def max_containers(a, b, c, x, y, z):
    max_cont = 0

    for h, l, w in [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, b, a), (c, a, b)]:
        if h <= z:
            quant_cont_width = y // w 
            quant_cont_height = x // l

            total_cont = quant_cont_width * quant_cont_height

            max_cont = max(max_cont, total_cont)

        return max_cont



a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

print(max_containers(a, b, c, x, y, z))