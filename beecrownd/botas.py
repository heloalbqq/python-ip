import sys
from collections import defaultdict

def count_pairs(boots):
    pairs = 0
    count = defaultdict(lambda: [0, 0])
    
    for size, side in boots:
        if side == 'D':
            count[size][0] += 1
        else:
            count[size][1] += 1
    
    for left, right in count.values():
        pairs += min(left, right)
    
    return pairs

def main():
    input = sys.stdin.read()
    data = input.strip().split('\n')
    
    index = 0
    while index < len(data):
        N = int(data[index])
        index += 1
        
        boots = []
        for _ in range(N):
            size, side = data[index].split()
            size = int(size)
            boots.append((size, side))
            index += 1
        
        result = count_pairs(boots)
        print(result)

if __name__ == "__main__":
    main()
