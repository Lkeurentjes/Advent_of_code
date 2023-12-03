import numpy as np


class Grid:
    def __init__(self, lines):

        self.blizzards = {">": [], "<": [], "^": [], "v": []}
        self.blizzardsdir = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
        self.height = len(lines)
        self.width = max(len(l) for l in lines)
        self.map = np.zeros((self.height, self.width))
        self.makemap(lines)
        self.start = (0, 1)
        self.finish = (self.height - 1, self.width - 2)
        self.routes = set({self.start})
        self.options = {(0, 1), (-1, 0), (1, 0), (0, -1), (0, 0)}

    def printgrid(self):
        for row in self.map:
            print("".join("#" if cell == 1 else "x" if cell == 9 else "." for cell in row))

    def makemap(self, lines):
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                if l == "#":
                    self.map[i][j] = 1
                elif l != ".":
                    self.map[i][j] = 9
                    self.blizzards[l].append((i, j))

    def blizzardsmove(self):
        self.map[self.map == 9] = 0
        for key, val in self.blizzards.items():
            x, y = self.blizzardsdir[key]
            newlocations = []
            for bx, by in val:
                xnew = bx + x
                ynew = by + y
                if 1 > xnew or xnew >= self.height - 1:
                    if x == -1:
                        xnew = self.height - 2
                    else:
                        xnew = 1
                if 1 > ynew or ynew >= self.width - 1:
                    if y == -1:
                        ynew = self.width - 2
                    else:
                        ynew = 1

                self.map[xnew][ynew] = 9
                newlocations.append((xnew, ynew))
            self.blizzards[key] = newlocations

    def move(self):
        round = 1
        while True:
            self.blizzardsmove()

            aftermove = set()
            for x, y in self.routes:
                for i, j in self.options:
                    if 0 <= x + i < self.height and 0 <= x + i < self.width:
                        if self.map[x+i][y+j] == 0:
                            aftermove.add((x+i, y+j))
            self.routes = aftermove

            if self.finish in self.routes:
                return round

            round += 1

    def move_finish_start_finish(self):
        round = 1
        goal = [self.finish, self.start, self.finish]
        goalnumber = 0
        while True:
            self.blizzardsmove()

            aftermove = set()
            for x, y in self.routes:
                for i, j in self.options:
                    if 0 <= x + i < self.height and 0 <= x + i < self.width:
                        if self.map[x+i][y+j] == 0:
                            aftermove.add((x+i, y+j))
            self.routes = aftermove

            if goal[goalnumber] in self.routes:
                if goalnumber == 2:
                    return round
                else:
                    self.routes.clear()
                    self.routes.add(goal[goalnumber])
                    goalnumber +=1

            round += 1


with open('2022-24-Blizard-Basin.txt') as f:
    lines = f.read().splitlines()

valley = Grid(lines)
valley2 = Grid(lines)
print("Part 1 the steps used to reach the end are", valley.move())
print("Part 2 the steps used to reach the end are", valley2.move_finish_start_finish())
