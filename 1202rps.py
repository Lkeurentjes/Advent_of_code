pointdict= {"X":1,"Y":2,"Z":3}
WindictX= {"A":3,"B":0,"C":6}
WindictY= {"A":6,"B":3,"C":0}
WindictZ= {"A":0,"B":6,"C":3}
with open("1202rps.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    points = 0
    for l in lines:
        points += pointdict[l[2]]
        if l[2] == "X":
            points+= WindictX[l[0]]
        if l[2] == "Y":
            points+= WindictX[l[0]]
        if l[2] == "Z":
            points+= WindictX[l[0]]
print(points)