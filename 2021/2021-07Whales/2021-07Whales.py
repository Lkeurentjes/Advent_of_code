from collections import Counter
def fuelpart1(positions, to):
    fuel_needed = 0
    positions_dict = Counter(positions)
    for key, value in positions_dict.items():
        if key < to:
            fuel_needed += (to - key) * value
        else:
            fuel_needed += (key - to) * value
    return fuel_needed

def fuelpart2(positions, to):
    fuel_needed = 0
    positions_dict = Counter(positions)
    for key, value in positions_dict.items():
        if key < to:
            fuel_needed += (to - key)*(to - key +1)/2 * value
        else:
            fuel_needed += (key - to)*(key - to +1)/2 * value
    return fuel_needed


with open('2021-07Whales.txt') as f:
    lines = f.read().splitlines()
    positions = list(map(int, lines[0].split(",")))

cost = []
for i in range(max(positions)):
    cost.append(fuelpart1(positions, i))

print("Part 1, the minimum fuel is", min(cost))

cost = []
for i in range(max(positions)):
    cost.append(fuelpart2(positions, i))
print("Part 1, the minimum fuel is", int(min(cost)))


