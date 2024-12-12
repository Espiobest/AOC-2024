from collections import defaultdict, deque

with open('data.txt', 'r') as region:
    lines = region.read().splitlines()

def get_neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_valid(coord):
    return 0 <= coord[0] < len(lines) and 0 <= coord[1] < len(lines[0])

coords = defaultdict(list)
visited = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if (i, j) in visited:
            continue

        c = lines[i][j]
        region = []
        queue = deque([(i, j)])
        cur_visited = set([(i, j)])
        while queue:
            x, y = queue.popleft()
            region.append((x, y))
            visited.add((x, y))

            for nx, ny in get_neighbors(x, y):
                if is_valid((nx, ny)) and lines[nx][ny] == c and (nx, ny) not in cur_visited:
                    queue.append((nx, ny))
                    cur_visited.add((nx, ny))

        coords[c].append(region)
     
part1 = 0
part2 = 0
for plant, regions in coords.items():
    for region in regions:
        region = set(region)
        area = len(region)
        perimeter = 0
        total_sides = 0
        for x, y in region:
            for side in get_neighbors(x, y):
                if side not in region:
                    perimeter += 1

        # count number of corners
        cor = 0
        total_corners = 0
        corner_offsets = [
            ((1, 1), [(0, 1), (1, 0)]),   # Bottom-right corner
            ((-1, -1), [(0, -1), (-1, 0)]),  # Top-left corner
            ((1, -1), [(0, -1), (1, 0)]),  # Bottom-left corner
            ((-1, 1), [(0, 1), (-1, 0)])   # Top-right corner
        ]
        for x, y in region:
            for (cx, cy), checks in corner_offsets:
                corner = (x + cx, y + cy)
                if all((x + dx, y + dy) not in region for dx, dy in checks):
                    total_corners += 1
                elif all((x + dx, y + dy) in region for dx, dy in checks) and corner not in region:
                    total_corners += 1

        total_sides += perimeter
        total_corners += cor

        part1 += area * total_sides
        part2 += area * total_corners

print("Part 1:", part1)
print("Part 2:", part2)