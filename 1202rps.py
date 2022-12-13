pointdict= {'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}
with open("1202rps.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    points = 0
    for l in lines:
        points += pointdict[l]

print(points)