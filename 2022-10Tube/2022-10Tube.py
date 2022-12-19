def check(cycle,X):
    if (cycle -20)%40 == 0:
        return (cycle*X)
    return 0

def add_crt(cycle,X):
    cyclerow = cycle% 40
    if cyclerow in range(X,X+3):
        if cyclerow == 0:
            return "#\n"
        return "#"
    if cyclerow == 0:
        return ".\n"
    return "."


with open('2022-10Tube.txt') as f:
    lines = f.read().splitlines()
    # print(lines)

transmitter = 0
cycle = 1
X = 1
crt = ""
crt += add_crt(cycle, X)
for line in lines:

    cycle += 1
    crt += add_crt(cycle, X)
    transmitter += check(cycle, X)
    if line == "noop":
        continue
    cycle +=1
    X += int(line.split(" ")[1])
    transmitter += check(cycle, X)
    crt += add_crt(cycle, X)

print("Part 1: sum of the signals =",transmitter)
print("Part 2: CRT look like:\n"+ crt)