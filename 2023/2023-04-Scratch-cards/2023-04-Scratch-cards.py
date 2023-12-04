from collections import Counter
with open('2023-04-Scratch-cards.txt') as f:
    lines = f.read().splitlines()

points = 0
cards = 0
cc = Counter(dict.fromkeys(range(1, len(lines) + 1),1))
for i,l in enumerate(lines):
    card, values_str = l.split(": ")
    values = [set(map(int, v.split())) for v in values_str.replace("  ", " ").split(" | ")]
    winning_numbers = values[0].intersection(values[1])
    points += 2 ** (len(winning_numbers)-1) if len(winning_numbers) != 0 else 0
    for j in range(cc[i+1]):
        cc.update(range(i+2, i+2+len(winning_numbers)))


print("Part 1, the points calculated is ",points)
print("Part 2, the number of cards is ",cc.total())
