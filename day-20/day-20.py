from collections import defaultdict, deque

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

grid = [list(line) for line in lines]
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'E':
            end = (i, j)
        if cell == 'S':
            start = (i, j)

def calculate(grid, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    queue = deque([(start, 0, [start])])
    costs = defaultdict(int)
    costs[start] = 0
    while queue:
        (x, y), steps, path = queue.popleft()
        visited.add((x, y))
        if (x, y) == end:
            final_path = path
            break
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if grid[new_x][new_y] != '#':
                    if (new_x, new_y) not in visited:
                      path.append((new_x, new_y))
                      queue.append(((new_x, new_y), steps + 1, path))
                      costs[new_x, new_y] = steps + 1
    return costs, final_path

costs, path = calculate(grid, start, end)

possible_cheats = [(0, 2), (2, 0), (0, -2), (-2, 0)]
cheat = defaultdict(int)

for cell in path:
   i, j = cell
   for d in possible_cheats:
      ni, nj = i + d[0], j + d[1]
      if (ni, nj) in costs:
        if costs[ni, nj] + 2 < costs[i, j]:
          cheat[(costs[i, j] - costs[ni, nj] - 2)] += 1

part1 = 0
for k, v in cheat.items():
    if k >= 100:
        part1 += v

print("Part 1:", part1)

part2 = 0
cheat = defaultdict(int)
possible_cheats = [(i, j) for i in range(-20, 21) for j in range(-20, 21) if abs(i) + abs(j) <= 20]

for cell in path:
    i, j = cell
    for d in possible_cheats:
        dx, dy = d
        ni, nj = i + dx, j + dy
        skip = abs(dx) + abs(dy)
        if (ni, nj) in costs:
            if costs[i, j] + skip < costs[ni, nj]:
                cheat[(costs[ni, nj] - costs[i, j] - skip)] += 1

for k, v in cheat.items():
    if k >= 100:
        part2 += v

print("Part 2:", part2)