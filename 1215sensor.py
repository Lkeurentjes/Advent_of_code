import numpy as np
from scipy.spatial import KDTree
import multiprocessing
import os
import time

RowToKnow = 2000000
# RowToKnow = 10
Rowlist = []
inputlist = []
maxX = 0
minX = 10000000000000000

def ManhattenDistance(v1, v2):
    return abs(v1[0]-v2[0]) + abs(v1[1] - v2[1])

with open("1215sensor.txt") as f:
    lines = f.read().splitlines()
    for i in range(len(lines)):
        line = lines[i].replace(",","").replace(":","").split(" ")
        # print(line)
        sensorX = int(line[2].split("=")[1])
        sensorY = int(line[3].split("=")[1])
        beaconX = int(line[8].split("=")[1])
        beaconY = int(line[9].split("=")[1])
        distance = ManhattenDistance((sensorX,sensorY),(beaconX, beaconY))
        inputlist.append([sensorX,sensorY,beaconX, beaconY, distance])
        if max(sensorX, beaconX) > maxX:
            maxX = max(sensorX, beaconX)
        if min(sensorX, beaconX) < minX:
            minX = min(sensorX, beaconX)
        # print(sensorX,sensorY,beaconX, beaconY, distance,maxX,minX)
maxX += 10000000
minX -= 10000000


width = abs(maxX - minX)
for i in range(width):
    Rowlist.append(None)

for input in inputlist:
    if input[1]-input[4]<RowToKnow and  input[1]+input[4]>RowToKnow:

        if input[3] == RowToKnow:
            Rowlist[input[2]-minX]=0

        addlength = input[4]-abs(input[1]-RowToKnow)

        for i in range(addlength+1):
            if  input[0] - i - minX >= 0:
                if Rowlist[input[0] - i - minX] is None:
                    Rowlist[input[0] - i - minX] = 1

            if  input[0] + i - minX < width:
                if Rowlist[input[0] + i - minX] is None:
                    Rowlist[input[0] + i - minX] = 1

sumanswer = 0
for item in Rowlist:
    if item is not None:
        sumanswer += item
print("answer to part 1: ",sumanswer, "\n")

viewblocked = []
for input in inputlist:
    viewblocked.append([input[0] - (input[4]//2),
                        input[0]+ (input[4]//2),
                        input[1]- (input[4]//2),
                        input[1]+ (input[4]//2)])

    viewblocked.append([input[0] - (input[4] // 2.5),
                        input[0] + (input[4] // 2.5),
                        input[1] - (input[4] // 1.66),
                        input[1] + (input[4] // 1.66)])
    viewblocked.append([input[0] - (input[4] // 1.66),
                        input[0] + (input[4] // 1.66),
                        input[1] - (input[4] // 2.5),
                        input[1] + (input[4] // 2.5)])

    viewblocked.append([input[0] - (input[4] // 3.33),
                        input[0] + (input[4] // 3.33),
                        input[1] - (input[4] // 1.4),
                        input[1] + (input[4] // 1.4)])
    viewblocked.append([input[0] - (input[4] // 1.4),
                        input[0] + (input[4] // 1.4),
                        input[1] - (input[4] // 3.33),
                        input[1] + (input[4] // 3.33)])

    viewblocked.append([input[0] - (input[4] // 2.5),
                        input[0] + (input[4] // 2.5),
                        input[1] - (input[4] // 1.66),
                        input[1] + (input[4] // 1.66)])
    viewblocked.append([input[0] - (input[4] // 1.66),
                        input[0] + (input[4] // 1.66),
                        input[1] - (input[4] // 2.5),
                        input[1] + (input[4] // 2.5)])

    viewblocked.append([input[0] - (input[4] // 5),
                        input[0] + (input[4] // 5),
                        input[1] - (input[4] // 1.25),
                        input[1] + (input[4] // 1.25)])
    viewblocked.append([input[0] - (input[4] // 1.25),
                        input[0] + (input[4] // 1.25),
                        input[1] - (input[4] // 5),
                        input[1] + (input[4] // 5)])

    viewblocked.append([input[0] - (input[4] // 10),
                        input[0] + (input[4] // 10),
                        input[1] - (input[4] // 1.1),
                        input[1] + (input[4] // 1.1)])
    viewblocked.append([input[0] - (input[4] // 1.1),
                        input[0] + (input[4] // 1.1),
                        input[1] - (input[4] // 10),
                        input[1] + (input[4] // 10)])

def subsetcheck(subsetX,subsetY,subset):
    for window in viewblocked:
        if window[0]<subsetX and window[1]>subsetX+subset and window[2]<subsetY and window[3]>subsetY+subset:
            return False


    allcoordinates = []
    start = time.time()
    Ypts = np.arange(subsetY, subsetY + subset)
    Xpts = np.arange(subsetX, subsetX + subset)
    X2D, Y2D = np.meshgrid(Ypts, Xpts)
    coordnp = np.column_stack((Y2D.ravel(), X2D.ravel()))
    completeset = {*range(subset * subset)}
    # print("i Am Here")
    print("making arrays", time.time()-start)

    start = time.time()
    treecoord = KDTree(coordnp)
    notset = set()
    for input in inputlist:
        starttree = KDTree([[input[0], input[1]]])
        indexes = starttree.query_ball_tree(treecoord, r=input[4], p=1)
        notset = notset.union(set(indexes[0]))
        if (len(notset) == subset * subset):
            print("making the tree en search until run", time.time() - start)
            return False

    answer = completeset.difference(notset)
    if answer != set():
        coord = coordnp[list(answer)[0]]
        print(answer, coordnp[list(answer)[0]])
        print("Answer to part 2: coord is", coord, "so answer is ", coord[0,0] * 4000000 + coord[0,1])
        return True



# print(inputlist)
def part2():
    maxXY = 4000000
    # maxXY = 20
    subset = 1000
    # subset = 5
    round =0

    starttime = time.time()
    for subsetX in range(0, maxXY,subset):
        for subsetY in range(0,maxXY,subset):
            round+=1

            if subsetcheck(subsetX,subsetY,subset):
                return
            if round%1000 == 0 :
                print("we are in round: ", round, "And we are " ,(time.time()-starttime)//60, "minutes in.")

    print("we facked up")

    # pool = multiprocessing.Pool()
    # pool.apply_async(subsetcheck,[(0,0,4000,1)])
    # for subsetX in range(0,maxXY,subset):
    #     for subsetY in range(0,maxXY,subset):
    #         round+=1
    #         pool.apply_async(subsetcheck,args=(subsetX,subsetY,subset,round))
    # pool.close()
    # pool.join
    # for i in range(0, 512):
    #     pool.apply_async(f, args=(i,))
    # pool.close()
    # pool.join()

    # result = pool.apply_async(f, [10])  # evaluate "f(10)" asynchronously
    # print
    # result.get(timeout=1)  # prints "100" unless your computer is *very* slow
    # print
    # pool.map(f, range(10))



part2()

# #part 2
# maxX = 4000000
# minX = 0
# width = abs(maxX - minX)
# row = []
# for j in range(width):
#     row.append(None)



# for checkrow  in range(width+1):
#     RowToKnow = checkrow
#     print(RowToKnow)
#     Rowlist = row.copy()
#
#     for input in inputlist:
#         if input[1]-input[4]<RowToKnow and  input[1]+input[4]>RowToKnow:
#             # print(input)
#             # if input[3] == RowToKnow:
#             #     Rowlist[input[2]-minX]=0
#
#             addlength = input[4]-abs(input[1]-RowToKnow)
#
#             # print(input, addlength)
#             for i in range(addlength+1):
#                 if  input[0] - i - minX >= 0 and input[0] - i - minX < width:
#                     if Rowlist[input[0] - i - minX] is None:
#                         Rowlist[input[0] - i - minX] = 1
#                 # print(input[0] + i - minX, width)
#                 if  input[0] + i - minX < width:
#                     if Rowlist[input[0] + i - minX] is None:
#                         Rowlist[input[0] + i - minX] = 1
#         if None not in Rowlist:
#             break
#
#
#     if None in Rowlist:
#         # print(Rowlist)
#         # print(Rowlist.index(None),RowToKnow)
#         print(Rowlist.index(None), RowToKnow, Rowlist.index(None) * 4000000 + RowToKnow)
#         break
#





# import re
#
# from z3 import If, Int, Solver
#
# with open("1215sensor.txt") as f:
#     ls = f.read().strip().split("\n")
#
# ns = [list(map(int, re.findall("-?\d+", x))) for x in ls]
#
#
# def manhattan(p1, p2):
#     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
#
#
# beacons = set()
# cants = set()
# y = 2000000
# for n in ns:
#     p1 = (n[0], n[1])
#     p2 = (n[2], n[3])
#     beacons.add(p2)
#     dist = manhattan(p1, p2)
#     for x in range(n[0] - dist, n[0] + dist + 1):
#         if manhattan(p1, (x, y)) <= dist:
#             cants.add((x, y))
#
# print(len(cants - beacons))
#
#
# # Part 2
# def z3abs(x):
#     return If(x >= 0, x, -x)
#
#
# s = Solver()
# x = Int("x")
# y = Int("y")
# s.add(x >= 0)
# s.add(x <= 4000000)
# s.add(y >= 0)
# s.add(y <= 4000000)
# for n in ns:
#     dist = manhattan((n[0], n[1]), (n[2], n[3]))
#     s.add(z3abs(x - n[0]) + z3abs(y - n[1]) > dist)
#
# s.check()
# model = s.model()
# print(model[x].as_long() * 4000000 + model[y].as_long())
