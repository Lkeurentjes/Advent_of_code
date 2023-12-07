import ast
import math

def explode(number, deptharray, i):
    # print("\ti need explode")
    exp, valL = deptharray[i]
    valR = deptharray[i + 1][1]

    if i-1 >= 0:
        c, n = deptharray[i-1]
        if len(c) == 1:
            number[c[0]] += valL
        elif len(c) == 2:
            number[c[0]][c[1]] += valL
        elif len(c) == 3:
            number[c[0]][c[1]][c[2]] += valL
        elif len(c) == 4:
            number[c[0]][c[1]][c[2]][c[3]] += valL
        elif len(c) == 5:
            number[c[0]][c[1]][c[2]][c[3]][c[4]] += valL
    if i+2 < len(deptharray):
        c, n = deptharray[i+2]
        if len(c) == 1:
            number[c[0]] += valR
        elif len(c) == 2:
            number[c[0]][c[1]] += valR
        elif len(c) == 3:
            number[c[0]][c[1]][c[2]] += valR
        elif len(c) == 4:
            number[c[0]][c[1]][c[2]][c[3]] += valR
        elif len(c) == 5:
            number[c[0]][c[1]][c[2]][c[3]][c[4]] += valR
    number[exp[0]][exp[1]][exp[2]][exp[3]] = 0
    # print("after explode",number)
    return reduce(number)


def split(number, change):
    # print("\ti need a split")
    ind, value = change
    val = [math.floor(value/2), math.ceil(value/2)]
    # number[tuple(ind)] = val
    if len(ind) == 1:
        number[ind[0]] = val
    elif len(ind) == 2:
        number[ind[0]][ind[1]] = val
    elif len(ind) == 3:
        number[ind[0]][ind[1]][ind[2]] = val
    elif len(ind) == 4:
        number[ind[0]][ind[1]][ind[2]][ind[3]] = val
    elif len(ind) == 5:
        number[ind[0]][ind[1]][ind[2]][ind[3]][ind[4]] = val
    # print("after split",number)
    return reduce(number)


def get_nested_indices_and_elements(lst, indices=None):
    if indices is None:
        indices = []
    result = []
    for i, el in enumerate(lst):
        if isinstance(el, list):
            result.extend(get_nested_indices_and_elements(el, indices + [i]))
        else:
            result.append((indices + [i], el))
    return result


def reduce(number):
    result = get_nested_indices_and_elements(number)
    for i, (index, element) in enumerate(result):
        if len(index) > 4:
            return explode(number, result, i)
    for i, (index, element) in enumerate(result):
        if element > 9:
            return split(number, result[i])
    # print("AFTER REDUCE    ",number)
    return number

def add(number, other):
    # print(([number, other]))
    number = reduce([number, other])
    return number

def magnitude(number):
    if isinstance(number, int):
        return number
    return magnitude(number[0]) * 3 + magnitude(number[1]) * 2

with open('2021-18-Snailfish-math.txt') as f:
    lines = f.read().splitlines()

snailsum = ast.literal_eval(lines[0])
for l in lines[1:]:
    output_list = ast.literal_eval(l)
    snailsum = add(snailsum, output_list)

print("part 1 has a magnitude of",magnitude(snailsum), "with the answer",snailsum)

max_magnitude = 0
for l in lines:
    for l2 in lines:
        if l == l2:
            continue
        out1 = ast.literal_eval(l)
        out2 = ast.literal_eval(l2)
        snailsum12 = add(out1, out2)
        max_magnitude = max(max_magnitude, magnitude(snailsum12))
print("Part 2, the max magnitude of the sum of 2 is",max_magnitude)
