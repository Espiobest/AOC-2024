from functools import cmp_to_key

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()
    rules = []
    numbers = []
    for line in lines:
        if "|" in line:
            rules.append([*map(int, line.split("|"))])
        elif "," in line:
            numbers.append([*map(int, line.split(","))])
    
valid = []
invalid = []

for n in numbers:
    ordered = True
    for a, b in rules:
        if a in n and b in n:
            if n.index(a) >= n.index(b):
                ordered = False

    if ordered:
        valid.append(n)
    else:
        invalid.append(sorted(n, key=cmp_to_key(lambda x,y: 1 if [x,y] in rules else -1)))


part1 = sum(x[len(x)//2] for x in valid)
part2 = sum(x[len(x)//2] for x in invalid)

print("Part 1:", part1)
print("Part 2:", part2)

