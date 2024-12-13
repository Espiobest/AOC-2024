import re

with open('data.txt', 'r') as r:
    lines = r.read().split('\n\n')

machines = []
for line in lines:
    a_match = re.search(r'Button A: X\+(\d+), Y\+(\d+)', line)
    a_x, a_y = map(int, a_match.groups())
    
    b_match = re.search(r'Button B: X\+(\d+), Y\+(\d+)', line)
    b_x, b_y = map(int, b_match.groups())
    
    prize_match = re.search(r'Prize: X=(\d+), Y=(\d+)', line)
    prize_x, prize_y = map(int, prize_match.groups())

    machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
    

def count_tokens(part2=False):
    tokens = 0
    for machine in machines:
        x, y, target = machine
        ax, ay = x
        bx, by = y
        px, py = target
        if part2:
            px += 10000000000000
            py += 10000000000000
        # solve a_x * x' + b_x * y' = prize_x and a_y * x' + b_y * y' = prize_y 
        # thx wolfram
        x_sol = (bx * py - by * px) / (bx * ay - ax * by)
        y_sol = (py - ay * x_sol) / by
        if int(x_sol) != x_sol or int(y_sol) != y_sol:
            continue

        tokens += 3 * x_sol + y_sol

    return tokens

part1 = int(count_tokens())
part2 = int(count_tokens(True))

print("Part 1:", part1)
print("Part 2:", part2)