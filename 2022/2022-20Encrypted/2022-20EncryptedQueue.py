from collections import deque

with open('2022-20Encrypted.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    # print(lines)

TOKNOW = [1000, 2000, 3000]

#PART 1
position_list = deque([(value, index) for index, value in enumerate(lines)])
for i, val in enumerate(lines):
    current_index = position_list.index((val, i))
    position_list.remove((val, i))
    position_list.rotate(-val)
    position_list.insert(current_index, (val, i))
check_list = list(map(lambda x: x[0], position_list))
zero_index = check_list.index(0)

print("PART 1: has", sum(check_list[(zero_index + i) % len(lines)] for i in TOKNOW), "as sum of the coordinates")

#PART 1
position_list = deque([(value*811589153, index) for index, value in enumerate(lines)])
for j in range(10):
    for i, val in enumerate(lines):
        val *= 811589153
        current_index = position_list.index((val, i))
        position_list.remove((val, i))
        position_list.rotate(-val)
        position_list.insert(current_index, (val, i))
check_list = list(map(lambda x: x[0], position_list))
zero_index = check_list.index(0)

print("PART 2: has", sum(check_list[(zero_index + i) % len(lines)] for i in TOKNOW), "as sum of the coordinates")



