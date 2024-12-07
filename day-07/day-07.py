import itertools
import multiprocessing

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

def solve(line, part2=False):
    test_value, nums = line.split(': ')
    test_value = int(test_value)
    nums = [*map(int, nums.split())]
    l = len(nums) - 1
    operations = ['+', '*']
    if part2:
        operations.append('||')
    ops = [*itertools.product(operations, repeat=l)]
    
    for op in ops:
        res = nums[0]
        for i, o in enumerate(op):
            if o == '+':
                res += nums[i+1]
            elif o == "*":
                res *= nums[i+1]
            else:
                res = int(str(res) + str(nums[i+1]))
        if res == test_value:
            return test_value
# 
    return 0

def solve2(line):
    return solve(line, part2=True)

if __name__ == "__main__":
        
    with multiprocessing.Pool() as pool:
        part1 = sum(pool.map(solve, lines))
        part2 = sum(pool.map(solve2, lines))

    print("Part 1:", part1)
    print("Part 2:", part2)