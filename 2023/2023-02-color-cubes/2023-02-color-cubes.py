with open('2023-02-color-cubes.txt') as f:
    lines = f.read().splitlines()

colordict = {"red": 12,
             "green": 13,
             "blue": 14}
sum = 0
power = 0
for l in lines:
    l = l.replace(":", "").replace(",", "").replace(";", "").split()
    good = True
    colorpowerdict = {"red": 0,"green": 0,"blue": 0}
    for i in range(2, len(l), 2):
        if int(l[i]) > colordict[l[i + 1]]:
            good = False
        if int(l[i]) > colorpowerdict[l[i + 1]]:
            colorpowerdict[l[i + 1]] = int(l[i])
    if good:
        sum += int(l[1])
    power += (colorpowerdict["red"] * colorpowerdict["green"] * colorpowerdict["blue"])

print("Part 1 is sum of id's is ", sum)
print("Part 2 is power of the minimum cubes is ", power)
