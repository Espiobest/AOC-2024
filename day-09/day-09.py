with open('data.txt', 'r') as r:
    nums = r.read()

data = []
dots = []
curID = 0
for i in range(len(nums)):
    num = int(nums[i])
    if i % 2 == 0:
        data.extend([curID] * num)
        curID += 1
    else:
        data.extend(['.'] * num)
        dots.extend(range(len(data)-num, len(data)))

data2 = data.copy()

for idx in dots:
    if idx > len(data):
        break
    val = data.pop()
    data[idx] = val
    while data[-1] == '.':
        data.pop()

part1 = 0
for i, e in enumerate(data):
    part1 += int(e) * i

print("Part 1:", part1)

# Part 2

dot_groups = []
for i in range(len(data2)):
    if data2[i] == '.':
        if i == 0 or data2[i - 1] != '.':
            dot_groups.append([i])
        else:
            dot_groups[-1].append(i)

file_data = []
i = 0
while i < len(data2):
    if data2[i] != '.':
        file_id = data2[i]
        start = i
        while i < len(data2) and data2[i] == file_id:
            i += 1
        size = i - start
        file_data.append((file_id, size, start))
    else:
        i += 1

file_data = file_data[::-1]
for file_id, size, start_index in file_data:
    for j, dots in enumerate(dot_groups):
        if len(dots) >= size and dots[0] < start_index:  
            for k in range(size):
                data2[dots[k]] = file_id
                data2[start_index + k] = '.'
            dot_groups[j] = dots[size:]
            if len(dot_groups[j]) == 0:
                dot_groups.pop(j)
            break

part2 = 0
for i, e in enumerate(data2):
    if e != '.':
        part2 += int(e) * i

print("Part 2:", part2)
