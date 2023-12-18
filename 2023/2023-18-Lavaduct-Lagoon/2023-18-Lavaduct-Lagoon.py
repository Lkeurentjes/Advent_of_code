import numpy as np
from itertools import tee
import sys

sys.setrecursionlimit(15000000)

class Grid:
    def __init__(self, lines):
        self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        # print(lines)
        self.border = self.get_border(lines)
        self.height = max([x for x, y in self.border]) + 1
        self.width = max([y for x, y in self.border]) + 1
        self.map = np.zeros((self.height, self.width))
        for x, y in self.border:
            self.map[x][y] = 1

    def get_border(self, lines):
        def translate_to_non_negative(b):
            minX = min([c[0] for c in b])
            minY = min([c[1] for c in b])
            b = [(x - minX, y - minY) for x, y in b]
            return b

        x, y = (0, 0)
        b = [(x, y)]
        for d, steps in lines:
            i, j = self.directions[d]
            for s in range(int(steps)):
                x += i
                y += j
                b.append((x, y))
        return translate_to_non_negative(b)

    def printgrid(self):
        for row in self.map:
            print("".join("■" if cell == 1 else "." if cell == 9 else "#" for cell in row))

    def count_inner(self):
        # loop around the corners and fill them till they reach border
        for x in [0, self.height - 1]:
            for y in range(self.width):
                if self.map[x][y] == 0:
                    self.flood_fill(x, y)
        for y in [0, self.width - 1]:
            for x in range(self.height):
                if self.map[x][y] == 0:
                    self.flood_fill(x, y)

        self.printgrid()
        return np.count_nonzero(self.map <= 1)

    def flood_fill(self, x, y):
        # fill
        if self.map[x][y] == 0:
            self.map[x][y] = 9
            for i, j in self.directions.values():
                if 0 <= x + i < self.height and 0 <= y + j < self.width:
                    self.flood_fill(x + i, y + j)


class Shoelace:
    def __init__(self, lines):
        self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.borderlength = 0
        self.border = self.get_border(lines)
        print(self.borderlength)

    def get_border(self, lines):
        x = y = 0
        b = []
        for d, steps in lines:
            self.borderlength += int(steps)
            i, j = self.directions[d]
            x += i * int(steps)
            y += j * int(steps)
            b.append((x,y))
        return b

    def pairwise(self, iterable):
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    def shoelace(self):
        area = 0
        for (x1, y1), (x2, y2) in self.pairwise(self.border):
            area += (x1 + x2) * (y1 - y2)
        return abs(area) // 2
    def solve(self):
        area = self.shoelace()
        return int(area - self.borderlength / 2 + 1) + self.borderlength



def translate_in_structions(color):
    dirdict = {"0": "R", "1": "D", "2": "L", "3": "U"}
    steps = int(color[2:-2], 16)
    d = dirdict[color[-2]]
    return [d, steps]


with open('2023-18-Lavaduct-Lagoon.txt') as f:
    lines = f.read().splitlines()
    linespt1 = [line.split(" ")[:-1] for line in lines]
    linespt2 = [translate_in_structions(c) for d, s, c in [line.split(" ") for line in lines]]
    print(linespt2)


lagoon = Grid(linespt1)
solverpt1 = Shoelace(linespt1)
solverpt2 = Shoelace(linespt2)
print("Part 1, count of the lagoon is", lagoon.count_inner())
print("\tMathematical way also for part 1", solverpt1.solve())
print("Part 2, count of the lagoon 2 is", solverpt2.solve())