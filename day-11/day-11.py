from collections import defaultdict

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()
    
nums = [*map(int, lines[0].split())]
count = {i: nums.count(i) for i in nums}
d = defaultdict(int)

def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        else:
            if len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                left = str(stone)[:half]
                right = str(stone)[half:]
                new_stones[int(left)] += count
                new_stones[int(right)] += count
            else:
                new_stones[stone * 2024] += count
    return new_stones

for i in range(1, 76):
    count = blink(count)
    if i == 25:
        print(f"Part 1: {sum(count.values())}")
    if i == 75:
        print(f"Part 2: {sum(count.values())}")

