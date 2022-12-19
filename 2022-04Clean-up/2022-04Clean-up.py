with open('2022-04Clean-up.txt') as f:
    lines = f.read().splitlines()
    # print(lines)

counter1 = 0
counter2= 0
for l in lines:
    l = list(map(int,l.replace("-",",").split(",")))
    #part 1
    if (l[0] >= l[2] and l[1] <= l[3]) or (l[2] >= l[0] and l[3] <= l[1]):
        counter1+=1

    #part 2
    if ((l[0] in range(l[2],l[3]+1)) or (l[1] in range(l[2],l[3]+1)) or (l[2] in range(l[0],l[1]+1)) or (l[3] in range(l[0],l[1]+1)) ):
        counter2 += 1

print("Part 1: ",counter1, "pairs fully contain the other")
print("Part 2: ",counter2, "pairs overlap the other")
