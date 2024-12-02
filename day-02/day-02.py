
def safe(lst):
    monotone = lst == sorted(lst) or lst == sorted(lst, reverse=True)
    if not monotone:
        return False
    for i, j in zip(lst, lst[1:]):
        if abs(i-j) < 1 or abs(i-j) > 3:
            return False
    return True

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()
    s = 0
    s2 = 0
    for i in lines:
        nums = [*map(int, i.split())]
        s += safe(nums)
        s2 += any(safe(nums[:j] + nums[j+1:]) for j in range(len(nums)))
    print("Part 1:", s)
    print("Part 2:", s2)