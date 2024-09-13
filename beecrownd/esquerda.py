import sys

def final_direction(commands):
    direction_map = 'NESW'
    current_index = 0 

    for command in commands:
        if command == 'E':
            current_index = (current_index - 1) % 4
        elif command == 'D':
            current_index = (current_index + 1) % 4
    
    return direction_map[current_index]

def main():
    input = sys.stdin.read().strip().split('\n')
    index = 0
    
    while index < len(input):
        N = int(input[index])
        if N == 0:
            break
        
        commands = input[index + 1]
        print(final_direction(commands))
        
        index += 2

if __name__ == "__main__":
    main()
