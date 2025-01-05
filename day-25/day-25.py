with open('data.txt', 'r') as r:
    lines = r.read().split("\n\n")

schemes = [line.splitlines() for line in lines]
locks = []
keys = []
for scheme in schemes:
    count = tuple(sum(scheme[row][col] == '#' for row in range(len(scheme))) for col in range(len(scheme[0])))
    if '#' in scheme[0]:
        locks.append(count)
    else:
        keys.append(count)

part1 = 0
for lock in locks:
    for key in keys:
        if all(l + k <= 7 for l, k in zip(lock, key)):
            part1 += 1

print("Part 1:", part1)
print("Part 2: Merry Christmas!")