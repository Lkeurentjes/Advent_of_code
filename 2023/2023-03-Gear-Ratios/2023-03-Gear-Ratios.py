with open('2023-03-Gear-Ratios.txt') as f:
    lines = f.read().splitlines()

locations = [(i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if not char.isdigit() and char != "."]
gears = {(i, j): [] for i, line in enumerate(lines) for j, char in enumerate(line) if char == "*"}

sum = 0
for i in range(len(lines)):
    number = ""
    start = 0
    last = ""
    for j in range(len(lines[0])):
        if lines[i][j].isdigit():
            number += lines[i][j]
            if not last.isdigit():
                start = j
            if j == len(lines[0])-1:
                found = False
                for Xc in range(i-1,i+2):
                    for Yc in range(start-1,j+1):
                        if (Xc, Yc) in locations:
                            if not found:
                                sum += int(number)
                            found = True
                            gears.get((Xc, Yc), []).append(int(number))


        else:
            if last.isdigit():
                found = False
                for Xc in range(i-1,i+2):
                    for Yc in range(start-1,j+1):
                        if (Xc, Yc) in locations:
                            if not found:
                                sum += int(number)
                            found = True
                            gears.get((Xc, Yc), []).append(int(number))


                number = ""
        last = lines[i][j]
print("Part 1, the sum of all gears parts is ",sum)

sum2 = 0
for items in gears.values():
    if len(items) == 2:
        sum2 += (items[0] * items[1])
print("Part 2, the sum of the multiplication real gears parts is ",sum2)