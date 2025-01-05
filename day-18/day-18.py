with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

size = 71
i = 1024
grid = [['.'] * (size + 1) for _ in range(size)]
for line in lines[:i]:
    x, y = map(int, line.split(','))
    grid[y][x] = '#'

while True:
    stack = [(0, 0, 0)]
    seen = set()
    found = False
    while stack:
        x, y, steps = stack.pop(0)
        if x == (size - 1) and y == (size - 1):
            if i == 1024:
                print("Part 1:", steps)
            found = True
            break
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] != '#':
                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    stack.append((nx, ny, steps + 1))
    if not found:
        break
    i += 1
    x, y = map(int, lines[i-1].split(','))
    grid[y][x] = '#'
    
print("Part 2:", lines[i-1])