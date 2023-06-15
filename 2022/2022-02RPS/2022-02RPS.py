pointdict1= {'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}
pointdict2= {'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}

with open('2022-02RPS.txt') as f:
    lines = f.read().splitlines()
    # print(lines)
    points1 = 0
    points2 = 0
    for l in lines:
        points1 += pointdict1[l]
        points2 += pointdict2[l]

print("Part 1: total points is", points1)
print("Part 2: total points is", points2)
