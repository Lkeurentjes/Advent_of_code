import numpy as np
class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.zeros((self.height, self.width))

        for i, c in enumerate(lines):
            for j, r in enumerate(lines[i]):
                if r == "#":
                    self.grid[i][j] = 1
        self.startgrid = self.grid.copy()
        self.rows = []
        self.col = 0
        self.expand()

    def printgrid(self):
        for row in self.grid:
            print("".join("★" if cell > 0 else "." for cell in row))

    def expand(self):
        self.rows = np.where(~self.grid.any(axis=1))[0]
        self.col = np.where(~self.grid.any(axis=0))[0]
        addrow = np.zeros((1, self.width))
        for i, r in enumerate(self.rows):
            self.grid = np.vstack((np.vstack((self.grid[0:r+i], addrow)),self.grid[r+i::]))
        self.height += len(self.rows)

        addcol = np.zeros((self.height, 1))
        for i, c in enumerate(self.col):
            self.grid = np.hstack((np.hstack((self.grid[:,0:c+i], addcol)),self.grid[:,c+i::]))
        self.width += len(self.col)

    def smallsum(self):
        x = list(np.where(self.grid == 1)[0])
        y = list(np.where(self.grid == 1)[1])
        stars = list(zip(x,y))
        sum = 0
        for i, (x,y) in enumerate(stars):
            for (xi,yi) in stars[i:]:
                sum += abs(x - xi) + abs(y - yi)
        return sum

    def bigsum(self, multiplier):
        x = list(np.where(self.startgrid == 1)[0])
        y = list(np.where(self.startgrid == 1)[1])
        stars = list(zip(x,y))
        sum = 0
        for i, (x,y) in enumerate(stars):
            for (xi,yi) in stars[i+1:]:
                i = 0
                j = 0
                for r in self.rows:
                    if x < r < xi or xi < r < x:
                        i+=multiplier-1
                for c in self.col:
                    if y < c < yi or yi < c < y:
                        j+=multiplier-1
                sum += abs(x - xi) + abs(y - yi) + i + j
        return sum


with open('2023-11-Cosmic-expansion.txt') as f:
    lines = f.read().splitlines()

galaxy = Grid(lines)
print("Part 1, the distance sum is", galaxy.smallsum(), "\n\talso works with faster part 2 code", galaxy.bigsum(2))
print("Part 2, the distance sum is", galaxy.bigsum(1000000))