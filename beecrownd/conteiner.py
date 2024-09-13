
A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())


def max_containers(container_width, container_length, container_height, ship_width, ship_length, max_height):
    if container_height > max_height:
        return 0
    max_width_fit = ship_width // container_width
    max_length_fit = ship_length // container_length
    return max_width_fit * max_length_fit

result = 0
result = max(result, max_containers(A, B, C, X, Y, Z))
result = max(result, max_containers(A, C, B, X, Y, Z))
result = max(result, max_containers(B, A, C, X, Y, Z))
result = max(result, max_containers(B, C, A, X, Y, Z))
result = max(result, max_containers(C, A, B, X, Y, Z))
result = max(result, max_containers(C, B, A, X, Y, Z))

print(result)
