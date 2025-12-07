import numpy as np
from functools import lru_cache


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array(lines)

        self.splitters = set()
        for i in range(self.height):
            for j in range(self.width):
                if lines[i][j] == '^':
                    self.splitters.add((i, j))
                if lines[i][j] == 'S':
                    self.start = (i, j)

        self.visitedSplitters = set()
        self.timelines = self.Beams(self.start)

    @lru_cache(maxsize=None)
    def Beams(self, position):
        x, y = position
        if x + 1 == self.height:
            return 1

        if (x + 1, y) in self.splitters:
            self.visitedSplitters.add((x + 1, y))
            total = 0
            # Split
            total += self.Beams((x + 1, y + 1))
            total += self.Beams((x + 1, y - 1))
            return total
        else:
            return self.Beams((x + 1, y))


with open('2025-07-Laboratories.txt') as f:
    lines = f.read().splitlines()
    Tachyon = Grid(lines)
    print("Part 1, times split is", len(Tachyon.visitedSplitters))
    print("Part 2, number of timelines", Tachyon.timelines)
