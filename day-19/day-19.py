with open('data.txt', 'r') as r:
    lines = r.read().split("\n\n")

available = lines[0].split(", ")
available = set(available)
towels = lines[1].splitlines()

part1 = 0
part2 = 0

for towel in towels:
    memo = {}

    def count_ways(i):
        if i == 0:
            return 1
        if i in memo:
            return memo[i]
        
        total = 0
        for t in available:
            t_len = len(t)
            if i >= t_len and towel[i - t_len:i] == t:
                total += count_ways(i - t_len)
        memo[i] = total
        return total

    ways = count_ways(len(towel))
    part1 += ways > 0
    part2 += ways

print("Part 1:", part1)
print("Part 2:", part2)