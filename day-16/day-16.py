from collections import deque
import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

grid = [list(line) for line in lines]

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == 'S':
            start = (i, j)
        if c == 'E':
            end = (i, j)

def dijkstra(start):
    queue = []
    loc = (start[0], start[1], 0)

    heapq.heappush(queue, (0, loc))
    visited = {loc: 0}
    while queue:
        points, (x, y, cur_dir) = heapq.heappop(queue)
        if (x, y, cur_dir) in visited and visited[(x, y, cur_dir)] < points:
            continue

        # move forward
        dx, dy = DIRECTIONS[cur_dir]
        nx, ny = x + dx, y + dy
        new_points = points + 1

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
            old_score = visited.get((nx, ny, cur_dir), float('inf'))
            if new_points < old_score:
                visited[(nx, ny, cur_dir)] = new_points
                heapq.heappush(queue, (new_points, (nx, ny, cur_dir)))            
        
        # rotate clockwise
        new_points = points + 1000
        new_dir = (cur_dir + 1) % 4
        if new_points < visited.get((x, y, new_dir), float('inf')):
            visited[(x, y, new_dir)] = new_points
            heapq.heappush(queue, (new_points, (x, y, new_dir)))

        # rotate counterclockwise
        new_dir = (cur_dir - 1) % 4
        if new_points < visited.get((x, y, new_dir), float('inf')):
            visited[(x, y, new_dir)] = new_points
            heapq.heappush(queue, (new_points, (x, y, new_dir)))
    
    return visited



visited = dijkstra(start)
end_points = [(k, v) for k, v in visited.items() if k[0] == end[0] and k[1] == end[1]]
part1 = min(end_points, key=lambda x: x[1])[1]
print("Part 1:", part1)

# part 2
# go backwards from all end points
shortest_path = set()
q = deque()
for d in range(4):
    if (end[0], end[1], d) in visited and visited[(end[0], end[1], d)] == part1:
        q.append((end[0], end[1], d))
        shortest_path.add((end[0], end[1], d))

while q:
    x, y, d = q.popleft()
    points = visited[(x, y, d)]

    dx, dy = DIRECTIONS[d]
    nx, ny = x - dx, y - dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
        prev_points = points - 1
        if (nx, ny, d) in visited and visited[(nx, ny, d)] == prev_points:
            if (nx, ny, d) not in shortest_path:
                shortest_path.add((nx, ny, d))
                q.append((nx, ny, d))

    new_points = points - 1000
    new_dir = (d - 1) % 4
    if (x, y, new_dir) in visited and visited[(x, y, new_dir)] == new_points:
        if (x, y, new_dir) not in shortest_path:
            shortest_path.add((x, y, new_dir))
            q.append((x, y, new_dir))
    
    new_dir = (d + 1) % 4
    if (x, y, new_dir) in visited and visited[(x, y, new_dir)] == new_points:
        if (x, y, new_dir) not in shortest_path:
            shortest_path.add((x, y, new_dir))
            q.append((x, y, new_dir))
    
unique_points = {(x, y) for x, y, _ in shortest_path}
part2 = len(unique_points)
print("Part 2:", part2)