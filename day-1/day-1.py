x, y = [], []
with open('data.txt', 'r') as r:
    lines = r.read().splitlines()
    for i in lines:
        a, b = map(int, i.split())
        x.append(a)
        y.append(b)

x.sort()
y.sort()
a = 0
b = 0
# part 1
for i, j in zip(x, y):
    a += abs(i - j)
# part 2
for i in x:
    b += y.count(i) * i
print("Part 1:", a)
print("Part 2:", b)
