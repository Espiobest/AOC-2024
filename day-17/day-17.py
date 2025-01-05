with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

registers = {'A': 0 , 'B': 0, 'C': 0}
program = []
for line in lines:
    if 'A' in line:
        registers['A'] = int(line.split(': ')[1])
    elif 'B' in line:
        registers['B'] = int(line.split(': ')[1])
    elif 'C' in line:
        registers['C'] = int(line.split(': ')[1])
    elif 'Program' in line:
        program = [*map(int, "".join(line.split(': ')[1]).split(','))]

def calculate(registers, program):
    i = 0
    output = [] 
    while i < len(program):
        op = program[i]
        literal =  program[i + 1]
        combo = program[i + 1]
        combo = {4: registers['A'], 5: registers['B'], 6: registers['C']}.get(combo, combo)
        if op == 0:
            registers['A'] = int(registers['A'] / (2 ** combo))
        elif op == 1:
            registers['B'] = registers['B'] ^ literal
        elif op == 2:
            registers['B'] = combo % 8
        elif op == 3:
            if registers['A'] == 0:
                i += 2
                continue
            else:
                i = literal
                continue
        elif op == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif op == 5:
            output.append(combo % 8)
        elif op == 6:
            registers['B'] = int(registers['A'] / (2 ** combo))
        elif op == 7:
            registers['C'] = int(registers['A'] / (2 ** combo))
        i += 2
  
    return output

output = calculate(registers, program)
part1 = ",".join(map(str, output))
print("Part 1:", part1)

# Part 2
'''
while a != 0
    b = a%8
    b = b^5
    c = a/(1<<b)
    a = a/(1<<3)
    b = b^c
    b = b^6
    output.append(b%8)
'''
# reset registers
registers['A'] = registers['B'] = registers['C'] = 0
stack = [(len(program) - 1, 0)]
part2 = []
# run program and move a_val by 3 bits to check chunks and keep running until all values match
while stack:
    offset, val = stack.pop(0)
    for cur in range(8):
        a_val = (val << 3) + cur
        registers['A'] = a_val
        if calculate(registers, program) == program[offset:]:
            if offset == 0:
                # all values match
                part2.append(a_val)
            stack.append((offset - 1, a_val))

print("Part 2:", min(part2))