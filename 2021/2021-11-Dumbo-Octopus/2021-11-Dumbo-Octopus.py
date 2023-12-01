import numpy as np
class Grid:
    def __init__(self, lines):
        self.alist = []
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(int(lines[i][j]))
            self.grid.append(row)

        self.add = np.ones((self.height, self.width))
        self.basin = np.zeros((self.height, self.width))
        self.lowestcoord = []

        self.adjacent = {(-1, 1), (0, 1), (1, 1), (-1, 0),
                         (1, 0), (-1, -1), (0, -1), (1, -1), (0, 0)}

    def printgrid(self):
        for i in self.grid:
            print(i)

    def recursive_flash(self):
        indexesX = np.where(self.grid == 10)[0].tolist()
        indexesY = np.where(self.grid == 10)[1].tolist()
        ind = 0
        while (ind != len(indexesX)):
            for x, y in self.adjacent:
                if 0 <= indexesX[ind] + x < self.height and 0 <= indexesY[ind] + y < self.width:
                    self.grid[indexesX[ind] + x][indexesY[ind] + y] += 1
                    if self.grid[indexesX[ind] + x][indexesY[ind] + y] == 10:
                        indexesX.append(indexesX[ind] + x)
                        indexesY.append(indexesY[ind] + y)

            ind += 1

    def flash_count(self):
        indexesX = np.where(self.grid >= 10)[0]
        indexesY = np.where(self.grid >= 10)[1]
        for i in range(len(indexesX)):
            self.grid[indexesX[i]][indexesY[i]] = 0
        return len(indexesX)

    def flashes(self, times):
        flashes = 0
        for i in range(times):
            self.grid += self.add
            self.recursive_flash()
            flashes += self.flash_count()
        return flashes

    def synchronise(self):
        i = 1
        while (True):
            self.grid += self.add
            self.recursive_flash()
            if self.height*self.width == self.flash_count():
                return i

            i += 1



with open('2021-11-Dumbo-Octopus.txt') as f:
    lines = f.read().splitlines()

sea = Grid(lines)
sea2 = Grid(lines)
print("Part 1 after 100 steps the number of flashes are: ", sea.flashes(100))
print("Part 2, they synchornise at step: ", sea2.synchronise())
