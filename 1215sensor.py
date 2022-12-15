# RowToKnow = 10
# Rowlist = []
# inputlist = []
# maxX = 0
# minX = 1000000000000000000000000000
#
# def ManhattenDistance(v1, v2):
#     return abs(v1[0]-v2[0]) + abs(v1[1] - v2[1])
#
# with open("1215sensor.txt") as f:
#     lines = f.read().splitlines()
#     for i in range(len(lines)):
#         line = lines[i].replace(",","").replace(":","").split(" ")
#         # print(line)
#         sensorX = int(line[2].split("=")[1])
#         sensorY = int(line[3].split("=")[1])
#         beaconX = int(line[8].split("=")[1])
#         beaconY = int(line[9].split("=")[1])
#         distance = ManhattenDistance((sensorX,sensorY),(beaconX, beaconY))
#         inputlist.append([sensorX,sensorY,beaconX, beaconY, distance])
#         if max(sensorX, beaconX) > maxX:
#             maxX = max(sensorX, beaconX)
#         if min(sensorX, beaconX) < minX:
#             minX = min(sensorX, beaconX)
#         # print(sensorX,sensorY,beaconX, beaconY, distance,maxX,minX)
# maxX += 10000000
# minX -= 10000000
#
#
# # width = abs(maxX - minX)
# # for i in range(width):
# #     Rowlist.append(None)
# #
# # # print(width,Rowlist)
# # for input in inputlist:
# #     if input[1]-input[4]<RowToKnow and  input[1]+input[4]>RowToKnow:
# #         # print(input)
# #         if input[3] == RowToKnow:
# #             Rowlist[input[2]-minX]=0
# #             # print("adding Beacon")
# #             # print(Rowlist)
# #         addlength = input[4]-abs(input[1]-RowToKnow)
# #         # print(addlength, input)
# #         print(input, addlength)
# #         for i in range(addlength+1):
# #             if  input[0] - i - minX >= 0:
# #                 if Rowlist[input[0] - i - minX] is None:
# #                     Rowlist[input[0] - i - minX] = 1
# #             # print(input[0] + i - minX, width)
# #             if  input[0] + i - minX < width:
# #                 if Rowlist[input[0] + i - minX] is None:
# #                     Rowlist[input[0] + i - minX] = 1
# #             # print(Rowlist)
# #         #     print("\n")
# #         # print("\n")
# #
# # print(minX, maxX)
# # sumanswer = 0
# # for item in Rowlist:
# #     if item is not None:
# #         sumanswer += item
# # print(sumanswer)
#
# #part 2
# maxX = 4000000
# minX = 0
# width = abs(maxX - minX)
# row = []
# for j in range(width):
#     row.append(None)
#
#
#
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
#
#
#
#
#
import re

from z3 import If, Int, Solver

with open("1215sensor.txt") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("-?\d+", x))) for x in ls]


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


beacons = set()
cants = set()
y = 2000000
for n in ns:
    p1 = (n[0], n[1])
    p2 = (n[2], n[3])
    beacons.add(p2)
    dist = manhattan(p1, p2)
    for x in range(n[0] - dist, n[0] + dist + 1):
        if manhattan(p1, (x, y)) <= dist:
            cants.add((x, y))

print(len(cants - beacons))


# Part 2
def z3abs(x):
    return If(x >= 0, x, -x)


s = Solver()
x = Int("x")
y = Int("y")
s.add(x >= 0)
s.add(x <= 4000000)
s.add(y >= 0)
s.add(y <= 4000000)
for n in ns:
    dist = manhattan((n[0], n[1]), (n[2], n[3]))
    s.add(z3abs(x - n[0]) + z3abs(y - n[1]) > dist)

s.check()
model = s.model()
print(model[x].as_long() * 4000000 + model[y].as_long())
