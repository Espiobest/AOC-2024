from collections import defaultdict

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

numbers = [*map(int, lines)]
part2nums = [x % 10 for x in numbers]
MOD = 16777216

def getPrices(x):
    prices = [x]
    for _ in range(2000):
        x = (x ^ (x * 64)) % MOD
        x = (x ^ (x // 32)) % MOD
        x = (x ^ (x * 2048)) % MOD
        prices.append(x)
    return prices

part1 = 0
S = defaultdict(int)

for number in numbers:
    prices = getPrices(number)
    part1 += prices[-1]

    prices = [*map(lambda x: x % 10, prices)]
    price_changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
    scores = {}
    for i in range(3, len(price_changes) - 1):
        cur_pattern = tuple(price_changes[i-3:i+1])
        if cur_pattern not in scores:
            scores[cur_pattern] = prices[i+1]

    for k, v in scores.items():
        S[k] += v

print("Part 1:", part1)
part2 = max(S.values())
print("Part 2:", part2)
