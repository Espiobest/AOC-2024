with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

grid = [[*map(int, line)] for line in lines]

def get_neighbors(x, y):
    return [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

start_vals = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            start_vals.append((i, j))

def get_paths(start, part2=False):
    score = 0
    stack = [start]
    visited = set()
    while stack:
        x, y = stack.pop()
        height = grid[x][y]
        if height == 9:
            if (x, y) not in visited or part2:
                score += 1
                visited.add((x, y))

        for nx, ny in get_neighbors(x, y):
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                continue
            if grid[nx][ny] == height + 1:
                stack.append((nx, ny))

    return score

part1 = 0
part2 = 0
for start in start_vals:
    part1 += get_paths(start)
    part2 += get_paths(start, part2=True)

print("Part 1:", part1)
print("Part 2:", part2)