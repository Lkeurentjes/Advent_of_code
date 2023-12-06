import math
def Optimized_count(T,D):
    last = T
    first = 0
    while True:
        if first * last > D:
            break
        first +=1
        last -=1
    return last - first +1

def distance(T,D):
    count, speed = 0, 0
    above = False
    for i in range(T):
        dist = (T-i) * speed
        if dist > D:
            above = True
            count+=1
        if dist < D and above:
            break
        speed +=1

    return count

with (open('2023-06-Boat-Race.txt') as f):
    lines = f.read().splitlines()
    pairs = list(zip([int(T) for T in lines[0].split()[1::]], [int(D) for D in lines[1].split()[1::]]))
    time = int("".join(filter(str.isdigit, lines[0])))
    dist = int("".join(filter(str.isdigit, lines[1])))

    # print(time,dist)

multiply = 1
for T, D in pairs:
    count = Optimized_count(T,D)
    multiply *= count

print("Part 1, the multiplication of the possiblities is: ",multiply)
print("Part 2, the possibilities for the big race",Optimized_count(time,dist))