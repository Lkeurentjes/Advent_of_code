import numpy as np


class Grid:
    def __init__(self, lines):
        self.valveslist = self.makelinesList(lines)
        self.diagonal = []
        self.max = self.valveslist.max(axis=0).max(axis=0)
        self.grid = np.zeros([self.max[0] + 1, self.max[1] + 1])
        self.addvalves()
        # print(self.grid)
        self.part1 = len(np.where(self.grid >= 2)[0])
        self.adddiagonals()
        # print(np.rot90(np.flip(self.grid, axis =1)))
        self.part2 = len(np.where(self.grid >= 2)[0])

    def makelinesList(self, lines):
        list = []
        for line in lines:
            xy = []
            for l in line.split(" -> "):
                l = l.split(",")
                l[0] = int(l[0])
                l[1] = int(l[1])
                xy.append(l)
            list.append(xy)
        return np.array(list)

    def addvalves(self):
        for valve in self.valveslist:
            # print(valve)
            if valve[0][0] == valve[1][0]:
                if valve[0][1] < valve[1][1]:
                    step = 1
                else:
                    step = -1
                for i in range(valve[0][1], valve[1][1] + step, step):
                    self.grid[valve[0][0], i] += 1

            elif valve[0][1] == valve[1][1]:
                if valve[0][0] < valve[1][0]:
                    step = 1
                else:
                    step = -1
                for i in range(valve[0][0], valve[1][0] + step, step):
                    self.grid[i, valve[0][1]] += 1

            else:
                self.diagonal.append(valve)

    def adddiagonals(self):
        for valve in self.diagonal:
            stepx = (valve[1][0] - valve[0][0])
            stepy = (valve[1][1] - valve[0][1])
            i, j = 1, 1
            if stepx < 0: i = -1
            if stepy < 0: j = -1
            for x, y in zip(range(0, stepx +i, i), range(0, stepy + j, j)):
                self.grid[valve[0][0] + x, valve[0][1] + y] += 1


with open('2021-05Hydrothermal-Venture.txt') as f:
    lines = f.read().splitlines()

oceanfloor = Grid(lines)
print("Part 1: there are", oceanfloor.part1, "Points with score 2 or more")
print("Part 2: there are", oceanfloor.part2, "Points with score 2 or more")
