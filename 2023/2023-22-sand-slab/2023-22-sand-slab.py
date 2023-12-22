import numpy as np
from functools import cache, cached_property
from queue import PriorityQueue
class Cube:
    def __init__(self, lines):
        self.blocks = {}
        self.leans_on = {}
        self.supports = {}

        self.maxX = max([l[0] for line in lines for l in line]) + 1
        self.maxY = max([l[1] for line in lines for l in line]) + 1
        tuples = [[("b",0) for y in range(self.maxY)] for x in range(self.maxX)]
        self.grid = np.array(tuples, dtype=np.dtype("<U99,int"))

        self.drop_sand()

    def printgrid(self):
        print("Grid")
        for row in self.grid:
            for r in row:
                print(r, end=""),
            print()

    def drop_sand(self):
        for i, (s, f) in enumerate(lines):
            i = str(i)

            above = []
            xstep = 1 if s[0] <= f[0] else -1
            for x in range(s[0],f[0]+1,xstep):
                ystep = 1 if s[1] <= f[1] else -1
                for y in range(s[1], f[1]+1, ystep):
                    above.append((x,y,self.grid[x][y]))

            newheight = max([a[2][1] for a in above]) +1
            for x,y, a in above:
                height = abs(f[2]-s[2]) # if more
                self.blocks[i] = (s,f)
                if newheight - 1 == a[1]:
                    self.leans_on.setdefault(i, set()).add(a[0])
                    self.supports.setdefault(a[0], set()).add(i)
                self.grid[x][y] = (i, newheight + height)

        print(self.leans_on)
        print(self.supports)

    def find_disintergrate(self):
        sum_dis = sum(1 for key in self.blocks.keys() if key not in self.supports)
        sum_dis += sum(1 for key in self.supports if all(len(self.leans_on[v]) == 1 for v in self.supports[key]))
        return sum_dis

    def _falcount(self,dis):
        if dis not in self.supports.keys():
            return 0
        Queue = PriorityQueue()
        Queue.put((0,dis))
        fallen = {dis}
        while not Queue.empty():
            p, dis = Queue.get()
            # print(dis)
            for v in self.supports[dis]:
                if v not in fallen:
                    fall = True
                    for i in self.leans_on[v]:
                        if i not in fallen:
                            fall = False
                    if fall:
                        fallen.add(v)
                        if v in self.supports.keys():
                            Queue.put((p+1, v))
        return len(fallen) - 1



    def dis_fall(self):
        return sum(self._falcount(key) for key in self.blocks.keys())


with open('2023-22-sand-slab.txt') as f:
    lines = f.read().splitlines()
    lines = [[list(map(int, l.split(","))) for l in line.split("~")] for line in lines]
    lines = sorted(lines, key=lambda item: min(item[0][2], item[1][2]))
sandfilter = Cube(lines)
print("Part 1, Number of disintergrated bricks", sandfilter.find_disintergrate())
print("Part 2, Number of bricks that would fall", sandfilter.dis_fall())
