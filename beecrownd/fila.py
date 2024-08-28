#nehuma pessoa entra mais na fila

entered = int(input())
num_enter = list(map(int, input().split()))

left = int(input())
num_left = list(map(int, input().split()))

num_left_set = set(num_left)

remained = [num for num in num_enter if num not in num_left_set]

print(" ".join(map(str, remained)))

