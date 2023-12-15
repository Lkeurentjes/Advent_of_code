def HASH(input, multiplier = 17, divider =256):
    val = 0
    for i in input:
        val += ord(i)
        val *= multiplier
        val %= divider
    return val

with open('2023-15-Lens-Library.txt') as f:
    lines = f.read().split(",")

sumHASH = 0
boxdict = {i: {} for i in range(0,256)}
for line in lines:
    sumHASH += HASH(line)
    if "=" in line:
        line = line.split("=")
        boxdict[HASH(line[0])][line[0]] = int(line[1])

    else:
        line = line.replace("-","")
        boxdict[HASH(line)].pop(line, None)

print("Part 1, the sum after the HASH algorithm is", sumHASH)

focus_power = 0
for box, items in enumerate(boxdict.values()):
    for i, value in enumerate(items.values()):
        focus_power += (box + 1) * (i + 1) * value
print("Part 2, the focus power is",focus_power)
