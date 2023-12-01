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

        self.basin = np.zeros((self.height, self.width))
        self.lowestcoord = []

    def printgrid(self):
        for i in self.grid:
            print(i)

    def getneighbours(self, i, j):
        neighbors = []

        # for i in range(len(self.grid)):
        #     for j, value in enumerate(self.grid[i]):

        if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
            # corners
            new_neighbors = []
            if i != 0:
                new_neighbors.append(self.grid[i - 1][j])  # top neighbor
            if j != len(self.grid[i]) - 1:
                new_neighbors.append(self.grid[i][j + 1])  # right neighbor
            if i != len(self.grid) - 1:
                new_neighbors.append(self.grid[i + 1][j])  # bottom neighbor
            if j != 0:
                new_neighbors.append(self.grid[i][j - 1])  # left neighbor

        else:
            # add neighbors
            new_neighbors = [
                self.grid[i - 1][j],  # top neighbor
                self.grid[i][j + 1],  # right neighbor
                self.grid[i + 1][j],  # bottom neighbor
                self.grid[i][j - 1]  # left neighbor
            ]

        # neighbors.append((value,new_neighbors))
        return new_neighbors

    def lowpointrisk(self):
        risk = 0
        for i in range(self.height):
            for j in range(self.width):
                neighbours = self.getneighbours(i, j)
                if min(neighbours) > self.grid[i][j]:
                    risk += (1 + self.grid[i][j])
                    self.lowestcoord.append([i, j])
        return risk

    def growbasin(self, i, j):
        if i < 0 or i >= self.height or j < 0 or j >= self.width:
            return 0
        elif self.grid[i][j] == 9:
            return 0
        elif self.basin[i][j] == 1:
            return 0
        else:
            self.basin[i][j] = 1
            top = self.growbasin(i - 1, j)
            right = self.growbasin(i, j + 1)
            down = self.growbasin(i + 1, j)
            left = self.growbasin(i, j - 1)
            return top + right + down + left + 1


    def basins(self):
        sizes = []
        # loop over the basins
        for c in self.lowestcoord:
            size = self.growbasin(c[0], c[1])
            sizes.append(size)
        sizes.sort(reverse=True)
        return sizes[0] * sizes[1] * sizes[2]


with open('2021-09-Lava-tube.txt') as f:
    lines = f.read().splitlines()

landscape = Grid(lines)
# landscape.printgrid()
print("PART 1: Lowest points risk is", landscape.lowpointrisk())
print("PART 2: multiplication of three largest basins", landscape.basins())
