with open('data.txt', 'r') as r:
    lines = r.read()

init, vals = lines.split("\n\n")

init = init.splitlines()
vals = vals.splitlines()

wires = {}

for wire in init:
    w, val = wire.split(": ")
    wires[w] = int(val)

seen = set()
sorted_wires = sorted(wires.items(), key=lambda x: x[0])
x_vals = "".join(str(v) for k, v in sorted_wires if k[0] == "x")[::-1]
y_vals = "".join(str(v) for k, v in sorted_wires if k[0] == "y")[::-1]

added = bin(int(x_vals, 2) + int(y_vals, 2))[2:]


while len(seen) != len(vals):
    for i, val in enumerate(vals):
        r, wire = val.split(" -> ")
        w1, op, w2 = r.split(" ")
        if w1 not in wires or w2 not in wires:
            continue
        if i in seen:
            continue
        if op == "AND":
            wires[wire] = wires[w1] & wires[w2]
        elif op == "OR":
            wires[wire] = wires[w1] | wires[w2]
        elif op == "XOR":
            wires[wire] = wires[w1] ^ wires[w2]
        seen.add(i)

wires = sorted(wires.items(), key=lambda x: x[0])
z_bin = "".join([str(val) for k, val in wires if k[0] == "z"])[::-1]
part1 = int(z_bin, 2)
print("Part 1:", part1)

# corrupt_bits = [len(added) - i for i in range(len(added)) if added[i] != z_bin[i]]
# print(corrupt_bits)
# part 2 had a bunch of debugging and solving by hand :(
