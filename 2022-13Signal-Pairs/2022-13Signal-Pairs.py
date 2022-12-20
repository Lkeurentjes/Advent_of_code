import json
from functools import cmp_to_key


def recursive_compare(left, right):
    if type(left) == int:
        if type(right) == int:
            return left - right
        return recursive_compare([left], right)
    if type(right) == int:
        return recursive_compare(left, [right])
    for l, r in zip(left, right):
        answer = recursive_compare(l, r)
        if answer != 0:
            return answer
    return len(left) - len(right)


sumpairs = 0

with open('2022-13Signal-Pairs.txt') as f:
    lines = f.read().splitlines()
    numberofpairs = (len(lines) + 1) // 3

all_pairs = []
PACKETS = [[[2]], [[6]]]

for i in range(numberofpairs):
    leftstr = lines[0 + i * 3]
    rightstr = lines[1 + i * 3]

    leftlist = json.loads(leftstr)
    rightlist = json.loads(rightstr)

    all_pairs.append(leftlist)
    all_pairs.append(rightlist)

    bool = recursive_compare(leftlist, rightlist)

    if recursive_compare(leftlist, rightlist) < 0:
        # print(i+1)
        sumpairs += (i + 1)
print("PART 1: the sum of all the indexes of correct pairs are", sumpairs)

all_pairs += PACKETS

# print(all_pairs)
all_pairs.sort(key=cmp_to_key(recursive_compare))
packet1 = all_pairs.index(PACKETS[0]) + 1
packet2 = all_pairs.index(PACKETS[1]) + 1
print("PART 2: the multiplication of the packet indexes is", packet1 * packet2)
# print(r * s)
