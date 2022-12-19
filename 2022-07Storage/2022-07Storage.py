# def recursivesize(sizes):
#     sumsize = sizes[0]
#     if sumsize <= 100000:
#         return sumsize
#     else:
#         for i in range(1,len(sizes)):
#             sumsize += recursivesize(drivesdict[sizes[i]])
#         if sumsize <= 100000:
#             return sumsize
#         else:
#             return 0
from collections import deque

def size_search(value, drivesdict,SIZE):
    currentsize = value[0]

    if currentsize > SIZE:
        return 0

    if len(value[1]) == 0:
        # print(currentsize)
        return currentsize

    queue = deque(value[1])
    while len(queue):
        search = queue.popleft()
        searchdrive = drivesdict[search]

        currentsize += searchdrive[0]
        if currentsize >= SIZE:
            return 0

        for tosearch in searchdrive[1]:
            queue.append(tosearch)


    # print(currentsize)
    return currentsize





with open('2022-07Storage.txt') as f:
    lines = f.read().splitlines()

drivesdict = {tuple(["/"]): [0, []]}
drivessize = 0
drivelist = []
dirnow = []
SIZE = 100000

for line in lines:
    line = line.split(" ")
    # print(line)

    if len(line) == 3:
        if line[2] == "..":
            dirnow.pop()
        else:
            dirnow.append(line[2])
            drivesdict[tuple(dirnow)] = [0,[]]
        continue

    if line[0] == "$":
        continue

    try:
        size = int(line[0])
    except:
        drivelist.append(tuple(dirnow))
        drivesdict[tuple(dirnow)][1].append(tuple(dirnow)+ (line[1],))
        drivesdict[tuple(dirnow)+ (line[1],)] = [0, []]
        continue
    drivesdict[tuple(dirnow)][0] += size

for drive, value in drivesdict.items():
    size = size_search(value, drivesdict,SIZE)
    drivessize += size

print("PART 1: total sum of drivesize of drives smaller then 100000  is", drivessize)

TOTAL = 70000000
NEEDED = 30000000
SIZE = TOTAL #not needed anymore

sizes = []
in_use= 0
for drive, value in drivesdict.items():
    size = size_search(value, drivesdict,SIZE)
    sizes.append((drive,size))
    if drive == tuple(["/"]):
        in_use = size

sorted_sizes = sorted(
    sizes,
    key=lambda t: t[1],
    reverse=False
)
for size in sorted_sizes:
    if TOTAL - (in_use - size[1]) >= NEEDED:
        print("PART 2: the drive to delete is",size[0], "and has size", size[1])
        break
