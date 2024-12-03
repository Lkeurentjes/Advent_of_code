import re


def extract_multiplications(memory):
    # regex pattern for multiplications
    pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    # makes a list with tuples of the integers
    matches = re.findall(pattern, memory)
    # sum the multiplication
    return sum(int(x) * int(y) for x, y in matches)


def extract_do_dont_mul(memory):
    #define all the paterns
    mul_pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize multiply bool and total score
    multiply = True
    total = 0

    # Sequentially process the memory string
    pos = 0
    while pos < len(memory):
        # Check for do
        do_match = re.match(do_pattern, memory[pos:])
        if do_match:
            multiply = True
            pos += do_match.end()
            continue

        # Check for don't
        dont_match = re.match(dont_pattern, memory[pos:])
        if dont_match:
            multiply = False
            pos += dont_match.end()
            continue

        # Check for mul(X, Y)
        mul_match = re.match(mul_pattern, memory[pos:])
        if mul_match:
            if multiply:
                x, y = int(mul_match.group(1)), int(mul_match.group(2))
                total += x * y
            pos += mul_match.end()
            continue

        # No match --> Move to the next
        pos += 1

    return total


with open('2024-03-Mull_It_Over.txt') as f:
    memory = f.read()
    print("Part 1, sum of multiplications is", extract_multiplications(memory))
    print("Part 2, sum of multiplications is", extract_do_dont_mul(memory))
