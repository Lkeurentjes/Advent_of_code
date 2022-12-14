with open("1204cleanup.txt") as f:
    lines = f.read().splitlines()
    print(lines)

counter = 0
for l in lines:
    l = list(map(int,l.replace("-",",").split(",")))
    print(l)
    # if (l[0] >= l[2] and l[1] <= l[3]) or (l[2] >= l[0] and l[3] <= l[1]):
    if ((l[0] in range(l[2],l[3]+1)) or (l[1] in range(l[2],l[3]+1)) or (l[2] in range(l[0],l[1]+1)) or (l[3] in range(l[0],l[1]+1)) ):
        counter += 1
print(counter)
