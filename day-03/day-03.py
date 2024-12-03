import re

with open('data.txt', 'r') as r:
    lines = r.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)", lines)
    part1 = sum(int(x) * int(y) for x, y in matches)
    print("Part 1:", part1)

    instructions = re.findall(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", lines)
    mul_enabled = True
    part2 = 0
    for instruction in instructions:
        if instruction[0] == "do()":
            mul_enabled = True
        elif instruction[0] == "don't()":
            mul_enabled = False
        elif "mul" in instruction[0] and mul_enabled:
            x, y = map(int, instruction[1:])
            part2 += x * y
    print("Part 2:", part2)

