from functools import cache

with open('data.txt', 'r') as r:
    code = r.read().splitlines()

keypad = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
          '4': (1, 0), '5': (1, 1), '6': (1, 2),
          '1': (2, 0), '2': (2, 1), '3': (2, 2),
          '0': (3, 1), 'A': (3, 2)}

dirpad = {'^': (0, 1), 'A': (0, 2),
          '<': (1, 0), 'v': (1, 1), '>': (1, 2)}


def build_path_graph(keypad, blocked_pos):
    paths = {}
    for start, (x1, y1) in keypad.items():
        for end, (x2, y2) in keypad.items():
            left = '<' * (y1 - y2)
            down = 'v' * (x2 - x1)
            up = '^' * (x1 - x2)
            right = '>' * (y2 - y1)
            
            path = left + down + up + right
            
            if blocked_pos in [(x1, y2), (x2, y1)]:
                path = path[::-1]
            
            paths[(start, end)] = path + 'A'
    
    return paths

num_paths = build_path_graph(keypad, (3, 0))
dir_paths = build_path_graph(dirpad, (0, 0))

@cache
def get_shortest_length(sequence, iterations, first=False):
    if iterations == 0:
        return len(sequence)
    
    cur_graph = num_paths if first else dir_paths
    
    length = 0
    prev = 'A'
    
    for char in sequence:
        length += get_shortest_length(cur_graph[(prev, char)], iterations - 1)
        prev = char
    
    return length

part1 = 0
part2 = 0
for buttons in code:
    numeric = int(buttons[:-1])
    part1 += numeric * get_shortest_length(buttons, 3, True)
    part2 += numeric * get_shortest_length(buttons, 26, True)

print("Part 1:", part1)
print("Part 2:", part2)