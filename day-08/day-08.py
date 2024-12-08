from collections import defaultdict

with open('data.txt', 'r') as r:
    grid = r.read().splitlines()

nodes = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        node = grid[i][j]
        if node != '.':
            nodes[node].append((i, j))

antinodes = set()
antinodes2 = set()
for node in nodes:
    coords = nodes[node]
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            # add antinode in the direction of x2, y2
            dx, dy = x2 - x1, y2 - y1
            x, y = x2 + dx, y2 + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                antinodes.add((x, y))
            
            antinodes2.add((x2, y2))
            while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                antinodes2.add((x, y))
                x += dx
                y += dy
        
            # add antinode in the direction of x1, y1
            dx2, dy2 = -dx, -dy
            x, y = x1 + dx2, y1 + dy2
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                antinodes.add((x, y))
            
            antinodes2.add((x1, y1))
            while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                antinodes2.add((x, y))
                x += dx2
                y += dy2
            
part1 = len(antinodes)
part2 = len(antinodes2)

print("Part 1:", part1)
print("Part 2:", part2)