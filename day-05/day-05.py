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
    
valid = 0
invalid = 0

for n in numbers:
    ordered = True
    for a, b in rules:
        if a in n and b in n:
            if n.index(a) >= n.index(b):
                ordered = False

    if ordered:
        valid += n[len(n) // 2]
    else:
        incorrect = sorted(n, key=cmp_to_key(lambda x,y: 1 if [x,y] in rules else -1))
        invalid += incorrect[len(incorrect) // 2]


print("Part 1:", valid)
print("Part 2:", invalid)

