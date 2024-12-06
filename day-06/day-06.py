from multiprocessing import Pool

with open('data.txt', 'r') as r:
    grid = r.read().splitlines()
    grid = [list(row) for row in grid]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            start = (i, j)
            break

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W

def path(grid, part2=False):
    pos = set()
    visited = set()
    nx, ny = start
    cur_dir = 0
    while True:
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
            break

        if grid[nx][ny] != "#":
            if part2 and (nx, ny, cur_dir) in visited:
                return None 
            visited.add((nx, ny, cur_dir))
            pos.add((nx, ny))
        else:
            nx -= DIR[cur_dir][0]
            ny -= DIR[cur_dir][1]
            cur_dir = (cur_dir + 1) % 4

        nx, ny = (nx + DIR[cur_dir][0], ny + DIR[cur_dir][1])

    return pos

def check_obstruction(pos, start, grid):
    x, y = pos
    if (x, y) == start:
        return 0

    grid2 = [row[:] for row in grid]
    grid2[x][y] = "#"
    if path(grid2, part2=True) is None:
        return 1

    return 0

if __name__ == "__main__":
    pos = path(grid)
    part1 = len(pos)
    print("Part 1:", part1)
    
    part2 = 0
    with Pool() as pool:
        part2_results = pool.starmap(check_obstruction, [(p, start, grid) for p in pos])

    part2 = sum(part2_results)
    print("Part 2:", part2)
