import numpy as np
class Grid:
    def __init__(self, lines):
        self.dots = [(int(x), int(y)) for l in lines for x, y in [l.split(",")]]
        self.height = max(x for x, _ in self.dots) + 1
        self.width = max(y for _, y in self.dots) + 1
        self.grid = np.zeros((self.width, self.height))
        for y,x in self.dots:
            self.grid[x][y]=1
    def printgrid(self):
        for row in self.grid:
            print("".join("■■" if cell > 0 else ".." for cell in row))

    def onefold(self, line):
        fold, line =line.split()[-1].split("=")
        line = int(line)
        if fold == "y":
            self.grid = self.grid[:line] + np.flipud(self.grid[line+1:])
        else:
            self.grid = self.grid[:, :line] + np.fliplr(self.grid[:, line+1:])
        return np.count_nonzero(self.grid)

    def folding(self, lines):
        for line in lines:
            self.onefold(line)

with open('2021-13-Origami.txt') as f:
    lines = f.read().splitlines()
    index = lines.index("")


Paper = Grid(lines[:index])
print("part 1, the number of dots remaning ", Paper.onefold(lines[index+1]))
Paper.folding(lines[index+2:])
print("part 2, the code can be seen below:")
Paper.printgrid()