with open('2021-02Dive.txt') as f:
    lines = f.read().splitlines()

horizontal = 0
depth = 0
aim = 0
depth2 = 0

for line in lines:
    line = line.split(" ")
    if line[0] == "forward":
        horizontal += int(line[1])
        depth2 += aim * int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
        aim += int(line[1])
    else:
        depth -= int(line[1])
        aim -= int(line[1])

print("PART 1: horizontal =",horizontal," and depth =", depth, "so the product =", horizontal*depth )
print("PART 2: horizontal =",horizontal," and depth =", depth2, "so the product =", horizontal*depth2 )



