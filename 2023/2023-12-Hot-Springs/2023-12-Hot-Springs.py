from functools import cache
@cache  # remembers when part of line is already been in the function, so builds "knowledge" over time
def count_options(line):
    springs, groups = line
    if len(groups) == 0:
        return 1 if "#" not in springs else 0
    elif springs == "" or groups[0] > len(springs):
        return 0

    if springs[0] == ".":
        return count_options((springs[1:], groups))

    elif springs[0] == "#":
        size = groups[0]
        if all(springs[i] != "." for i in range(size)):
            if len(springs) == size:
                return 1 if len(groups) == 1 else 0
            if springs[size] != "#":
                return count_options(("." + springs[size + 1:], groups[1:]))
        return 0

    else:  # == "?" the try both
        return count_options(("." + springs[1:], groups)) + count_options(("#" + springs[1:], groups))

with open('2023-12-Hot-Springs.txt') as f:
    lines = f.read().splitlines()
    lines = [(line[0], tuple(map(int, line[1].split(',')))) for line in [line.split() for line in lines]]
    lines5 = [(line[0] + ("?" + line[0]) * 4, line[1] * 5) for line in lines]

sumpt1, sumpt2 = 0, 0
for i, line in enumerate(lines):
    sumpt1 += count_options(line)
    sumpt2 += count_options(lines5[i])
print("the sum of part 1 is", sumpt1)
print("the sum of part 2 is", sumpt2)
