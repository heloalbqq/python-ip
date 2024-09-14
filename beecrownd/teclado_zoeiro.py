def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    first_line = data[0].split()
    N = int(first_line[0])
    M = int(first_line[1])
 
    key_map = {}

    index = 1
    for _ in range(N):
        E, S = data[index].split()
        key_map[E] = S
        index += 1

    reverse_key_map = {v: k for k, v in key_map.items()}

    results = []
    for _ in range(M):
        phrase = data[index]
        corrected_phrase = ''.join(reverse_key_map.get(c, c) for c in phrase)
        results.append(corrected_phrase)
        index += 1

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
