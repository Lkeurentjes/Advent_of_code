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

        # self.printgrid()
        self.vissablelr = np.zeros((self.height, self.width))
        self.vissablerl = np.zeros((self.height, self.width))
        self.vissableud = np.zeros((self.height, self.width))
        self.vissabledu = np.zeros((self.height, self.width))
        self.visablenumber = 0

        self.treehousevalues = np.zeros((self.height, self.width))

    def printgrid(self):
        for i in self.grid:
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
            seevalue = self.grid[i][self.height - 1]
            for j in range(self.width - 1, 0, -1):
                if j == self.width - 1:
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
            seevalue = self.grid[self.width - 1][i]
            for j in range(self.height - 1, 0, -1):
                if j == self.height - 1:
                    self.vissabledu[j][i] = 1
                if self.vissableud[j][i] == 1:
                    break
                if self.grid[j][i] > seevalue:
                    self.vissabledu[j][i] = 1
                    seevalue = self.grid[j][i]
                if self.grid[j][i] == 9:
                    break

        # print(self.vissablelr)
        # print(self.vissableud)
        # print(self.vissablerl)
        # print(self.vissabledu)
        # print(self.vissablelr+self.vissableud+self.vissablerl+self.vissabledu)
        return (np.count_nonzero(self.vissablelr + self.vissableud + self.vissablerl + self.vissabledu))

    def treehouse(self):
        best = 0
        for i in range(self.height):

            for j in range(self.width):
                score = 1
                viewvertical = [[*range(i-1,-1, -1)], [*range(i + 1, self.height)]]
                for view in viewvertical:
                    scorev = 0
                    height = self.grid[i][j]
                    for v in view:
                        if self.grid[v][j] < height:
                            scorev += 1

                        else:
                            scorev += 1
                            break
                    # print("score: ",scorev)
                    score *= scorev

                viewhorizontal = [[*range(j-1,-1,-1)], [*range(j + 1, self.width)]]
                for view in viewhorizontal:
                    scorev = 0
                    height = self.grid[i][j]
                    for v in view:

                        if self.grid[i][v] < height:
                            scorev += 1

                        else:
                            scorev += 1
                            break
                    # print("score: ",scorev)
                    score *= scorev
                # print(score)

                best = max(score, best)
        return best


with open('2022-08Treehouse.txt') as f:
    lines = f.read().splitlines()

landscape = Grid(lines)
print("PART 1: Trees vissable from the outside are", landscape.visability())
print("PART 2: best location has a scenic view of", landscape.treehouse())
