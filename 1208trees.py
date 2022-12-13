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

        self.printgrid()
        self.vissablelr = np.zeros((self.height, self.width))
        self.vissablerl = np.zeros((self.height, self.width))
        self.vissableud = np.zeros((self.height, self.width))
        self.vissabledu = np.zeros((self.height, self.width))
        self.visablenumber = 0

        self.treehousevalues = np.zeros((self.height, self.width))


    def printgrid(self):
        for i in self.grid:
            # pass
            print(i)

    def visability(self):

        # left
        for i in range(self.height):
            seevalue = self.grid[i][0]
            for j in range(self.width):
                if j == 0:
                    self.vissablelr[i][j] = 1
                if self.grid[i][j] > seevalue:
                    self.vissablelr[i][j] = 1
                    seevalue = self.grid[i][j]
                if self.grid[i][j] == 9:
                    break

        # up
        for i in range(self.width):
            seevalue = self.grid[0][i]
            for j in range(self.height):
                if j == 0:
                    self.vissableud[j][i] = 1
                if self.grid[j][i] > seevalue:
                    self.vissableud[j][i] = 1
                    seevalue = self.grid[j][i]

                if self.grid[j][i] == 9:
                    break

        # right
        for i in range(self.height):
            seevalue = self.grid[i][self.height-1]
            for j in range(self.width-1,0,-1):
                if j == self.width-1:
                    self.vissablerl[i][j] = 1

                if self.vissablelr[i][j] == 1:
                    break

                if self.grid[i][j] > seevalue:
                    self.vissablerl[i][j] = 1
                    seevalue = self.grid[i][j]
                if self.grid[i][j] == 9:
                    break

        # down
        for i in range(self.width):
            seevalue = self.grid[self.width-1][i]
            for j in range(self.height-1,0,-1):
                if j == self.height-1:
                    self.vissabledu[j][i] = 1

                if self.vissableud[j][i] ==1:
                    break

                if self.grid[j][i] > seevalue:
                    self.vissabledu[j][i] = 1
                    seevalue = self.grid[j][i]

                if self.grid[j][i] == 9:
                    break


        # # print(self.vissablelr)
        # # print(self.vissableud)
        # # print(self.vissablerl)
        # # print(self.vissabledu)
        # print(self.vissablelr+self.vissableud+self.vissablerl+self.vissabledu)
        # # print(np.count_nonzero(self.vissablelr + self.vissableud + self.vissablerl + self.vissabledu))

    def treehouse(self):
        for i in range(self.height):
            for j in range(self.width):
                tree = self.grid[i][j]
        best = 0
        # for y, row in enumerate(self.grid):
        #     for x, tree in enumerate(row):
        #         # views = [self.grid[y][:x][::-1], self.grid[y][x + 1:], T[x][:y][::-1], T[x][y + 1:]]
        #         score = 1
        #         for view in views:
        #             try:
        #                 score *= list(v >= tree for v in view).index(True) + 1
        #             except ValueError:
        #                 score *= len(view)
        #         best = max(score, best)
        # print(best)



with open("1208trees.txt") as f:
    lines = f.read().splitlines()
    landscape = Grid(lines)
    # landscape.visability()
    landscape.treehouse()

with open('1208trees.txt') as f:
    A = list(f.read().strip().splitlines())

A = [[int(c) for c in line.strip()] for line in A]
T = list(zip(*A))

best = 0
for y, row in enumerate(A):
    for x, tree in enumerate(row):
        views = [A[y][:x][::-1], A[y][x + 1:], T[x][:y][::-1], T[x][y + 1:]]
        score = 1
        for view in views:
            try:
                score *= list(v >= tree for v in view).index(True) + 1
            except ValueError:
                score *= len(view)
        best = max(score, best)
print(best)