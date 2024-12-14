from PIL import Image, ImageDraw
import re

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

width = 101
height = 103

grid = [[0] * width for _ in range(height)]
robots = []
for line in lines:
    x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
    grid[y][x] += 1
    robots.append((x, y, vx, vy))

robots2 = robots.copy()

for i in range(100):
    new_robots = []
    for x, y, vx, vy in robots:
        grid[y][x] -= 1
        x = (x + vx) % width
        y = (y + vy) % height
        grid[y][x] += 1
        new_robots.append((x, y, vx, vy))
    robots = new_robots

tl = 0
tr = 0
bl = 0
br = 0
for robot in robots:
    x, y, _, _ = robot
    if x < width // 2 and y < height // 2:
        tl += 1
    elif x > width // 2 and y < height // 2:
        tr += 1
    elif x < width // 2 and y > height // 2:
        bl += 1
    elif x > width // 2 and y > height // 2:
        br += 1

part1 = tl * tr * bl * br
print("Part 1:", part1)

# part 2
i = 0
grid_list = []
while True:
    i += 1
    new_robots = []
    seen = set()
    grid = [['.'] * width for _ in range(height)]
    for x, y, vx, vy in robots2:
        x = (x + vx) % width
        y = (y + vy) % height
        new_robots.append((x, y, vx, vy))
        seen.add((x, y))
        grid[y][x] = '#'
    
    if len(seen) == len(new_robots):
        break
    robots2 = new_robots
    if i % 1000 == 0:
        grid_list.append(grid)

grid_list.append(grid)
part2 = i
print("Part 2:", part2)
# display the grid

for row in grid:
    print(''.join(row))

# create a gif
images = []
dot_size = 5
for grid in grid_list:
    img = Image.new('RGB', (width * 10, height * 10), color='black')
    draw = ImageDraw.Draw(img)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                x0 = x * 10 - dot_size // 2
                y0 = y * 10 - dot_size // 2
                x1 = x * 10 + dot_size // 2
                y1 = y * 10 + dot_size // 2
                draw.ellipse((x0, y0, x1, y1), fill='green')

    images.append(img)

images[0].save('animation.gif', save_all=True, append_images=images[1:], duration=100, loop=0)