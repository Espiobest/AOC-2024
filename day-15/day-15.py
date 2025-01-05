from collections import defaultdict

with open('data.txt', 'r') as r:
    lines = r.read().split('\n\n')

grid = [list(line) for line in lines[0].split('\n')]
moves = ''.join(lines[1].split('\n'))
DIRECTIONS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def move_robot(grid, robot, boxes):
    x, y = robot
    for move in moves:
        dx, dy = DIRECTIONS[move]
        new_x, new_y = x + dx, y + dy
        next_x, next_y = new_x, new_y

        if not in_bounds(new_x, new_y, grid):
            continue

        if grid[new_x][new_y] == '#':
            continue

        box_list = []
        while (new_x, new_y) in boxes:
            box_list.append((new_x, new_y))
            new_x += dx
            new_y += dy

        if not in_bounds(new_x, new_y, grid):
            continue
        if grid[new_x][new_y] == '#' or (new_x, new_y) in boxes:
            continue

        for box in box_list[::-1]:
            boxes.remove(box)
            bx = box[0] + dx
            by = box[1] + dy
            boxes.add((bx, by))

        x, y = next_x, next_y

    return boxes

boxes = set()
for x, row in enumerate(grid):
    for y, cell in enumerate(row):
        if cell == 'O':
            boxes.add((x, y))
        if cell == '@':
            robot = (x, y)

part1 = 0
box_positions = move_robot(grid, robot, boxes)
for box in box_positions:
    x, y = box
    part1 += 100 * x + y

print("Part 1:", part1)

# Part 2

scaled_grid = []
for row in grid:
    new_row = []
    for tile in row:
        if tile == '#': 
            new_row.extend(['#', '#'])
        elif tile == 'O':
            new_row.extend(['[', ']'])
        elif tile == '.':
            new_row.extend(['.', '.'])
        elif tile == '@':
            new_row.extend(['@', '.'])
    scaled_grid.append(new_row)

for x, row in enumerate(scaled_grid):
    for y, cell in enumerate(row):
        if cell == '@':
            scaled_grid[x][y] = '.'
            robot = (x, y)

def move_boxes(robot, moves, grid):
    for move in moves:
        i, j = robot
        if move == '<':
            k = j-1
            while grid[i][k] == ']':
                k -= 2
            if grid[i][k] == '.':
                for b in range(k, j):
                    grid[i][b] = grid[i][b+1]
                new_robot = (i, j-1)
                
        elif move == '>':
            k = j+1
            while grid[i][k] == '[':
                k += 2
            if grid[i][k] == '.':
                for b in range(k, j, -1):
                    grid[i][b] = grid[i][b-1]
                new_robot = (i, j+1)
                
        elif move == '^':
            queue = {(i-1, j)}
            rows = defaultdict(set)
            blocked = False
            while queue and not blocked:
                x, y = queue.pop()
                cur = grid[x][y]
                if cur == '#':
                    blocked = True
                elif cur == ']':
                    rows[x].update({y-1, y})
                    queue.update({(x-1, y), (x-1, y-1)})
                elif cur == '[':
                    rows[x].update({y, y+1})
                    queue.update({(x-1, y), (x-1, y+1)})
                else:
                    rows[x].add(y)
                    
            if not blocked:
                for x in sorted(rows):
                    for y in rows[x]:
                        if y in rows[x+1]:
                            grid[x][y] = grid[x+1][y]
                        else:
                            grid[x][y] = '.'
                new_robot = (i-1, j)

        elif move == 'v':
            queue = {(i+1, j)}
            rows = defaultdict(set)
            blocked = False
            
            while queue and not blocked:
                x, y = queue.pop()
                cur = grid[x][y]
                if cur == '#':
                    blocked = True
                elif cur == ']':
                    rows[x].update({y-1, y})
                    queue.update({(x+1, y), (x+1, y-1)})
                elif cur == '[':
                    rows[x].update({y, y+1})
                    queue.update({(x+1, y), (x+1, y+1)})
                else:
                    rows[x].add(y)
                    
            if not blocked:
                for x in sorted(rows, reverse=True):
                    for y in rows[x]:
                        if y in rows[x-1]:
                            grid[x][y] = grid[x-1][y]
                        else:
                            grid[x][y] = '.'
                new_robot = (i+1, j)
        
        robot = new_robot
    
    boxes = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '[':
                boxes.add((i, j))

    return boxes

boxes = move_boxes(robot, moves, scaled_grid)
part2 = 0
for box in boxes:
    x, y = box
    part2 += 100 * x + y

print("Part 2:", part2)
