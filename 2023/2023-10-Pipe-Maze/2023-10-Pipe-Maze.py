import numpy as np

class Grid:
    def __init__(self, lines):
        self.alist = []
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = []
        self.start = (0, 0)
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(lines[i][j])
                if lines[i][j] == "S":
                    self.start = (i, j)
            self.grid.append(row)

        self.directionfrom = {(0, 1): "E", (-1, 0): "N", (1, 0): "S", (0, -1): "W"}

        self.loop = ()
        self.countgridL = np.zeros((self.height, self.width))
        self.countgridL[self.start] = 1

        self.countgridR = np.zeros((self.height, self.width))
        self.countgridR[self.start] = 1

        self.current = []
        self.dir = []
        for i, j in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
            x, y = self.start
            if 0 <= x + i < self.height and 0 <= y + j < self.width:
                self.current.append((x + i, y + j))
                self.dir.append(self.directionfrom[(i, j)])

        self.left = {"N": (0, -1), "S": (0, 1), "E": (-1, 0), "W": (1, 0)}
        self.right = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        self.directionfrom = {(0, 1): "E", (-1, 0): "N", (1, 0): "S", (0, -1): "W"}

        self.directionto = {"|": {"S": (1, 0), "N": (-1, 0)},
                            "-": {"E": (0, 1), "W": (0, -1)},
                            "L": {"S": (0, 1), "W": (-1, 0)},
                            "J": {"S": (0, -1), "E": (-1, 0)},
                            "7": {"N": (0, -1), "E": (1, 0)},
                            "F": {"N": (0, 1), "W": (1, 0)}}

        self.right = {"|": {"N": [(0, 1)], "S": [(0, -1)]},
                      "-": {"E": [(1, 0)], "W": [(-1, 0)]},
                      "L": {"S": [(0, -1), (1, -1), (1, 0)]},
                      "J": {"E": [(1, 0), (1, 1), (0, 1)]},
                      "7": {"N": [(0, 1), (-1, 1), (-1, 0)]},
                      "F": {"W": [(-1, 0), (-1, -1), (0, -1)]}}

        self.left = {"|": {"S": [(0, 1)], "N": [(0, -1)]},
                     "-": {"W": [(1, 0)], "E": [(-1, 0)]},
                     "L": {"W": [(0, -1), (1, -1), (1, 0)]},
                     "J": {"S": [(1, 0), (1, 1), (0, 1)]},
                     "7": {"E": [(0, 1), (-1, 1), (-1, 0)]},
                     "F": {"N": [(-1, 0), (-1, -1), (0, -1)]}}

    def printgrid(self):
        for i in self.grid:
            print(i)

    def walk(self):
        steps = 1
        while True:
            steps += 1
            discard = []
            for index, (x, y) in enumerate(self.current):
                go = self.grid[x][y]
                if go != "S" and go != "." and self.dir[index] in self.directionto[go].keys():
                    i, j = self.directionto[go][self.dir[index]]
                    if 0 <= x + i < self.height and 0 <= y + j < self.width:
                        self.current[index] = (x + i, y + j)
                        self.dir[index] = self.directionfrom[(i, j)]
                else:
                    discard.append(index)

            for d in sorted(discard, reverse=True):
                self.current.pop(d)
                self.dir.pop(d)

            if len(self.current) - len(set(self.current)) == 1:
                return steps
            # if steps == 3:
            #     break

    def inner(self):
        for (i, j), val in self.directionfrom.items():
            x, y = self.start
            if 0 <= x + i < self.height and 0 <= y + j < self.width:
                go = self.grid[x + i][y + j]
                if go != "S" and go != "." and val in self.directionto[go].keys():
                    self.loop = ((x + i, y + j), val)
                    self.countgridR[(x + i, y + j)] = 8
                    if val in self.right[go]:
                        for xi, yi in self.right[go][val]:
                            # xi, yi = self.right[self.directionfrom[(i, j)]]
                            if 0 <= x + i + xi < self.height and 0 <= y + j + yi < self.width and self.countgridR[
                                (x + i + xi, y + j + yi)] != 8:
                                self.countgridR[(x + i + xi, y + j + yi)] = 1

                    self.countgridL[(x + i, y + j)] = 8
                    if val in self.left[go]:
                        for xi, yi in self.left[go][val]:
                            # xi, yi = self.left[self.directionfrom[(i, j)]]
                            if 0 <= x + i + xi < self.height and 0 <= y + j + yi < self.width and self.countgridL[
                                (x + i + xi, y + j + yi)] != 8:
                                self.countgridL[(x + i + xi, y + j + yi)] = 1
                    break

        while self.loop[0] != self.start:
            (x, y), dir = self.loop
            go = self.grid[x][y]
            if go != "S" and go != "." and dir in self.directionto[go].keys():
                i, j = self.directionto[go][dir]
                if 0 <= x + i < self.height and 0 <= y + j < self.width:
                    self.loop = ((x + i, y + j), self.directionfrom[(i, j)])

                    self.countgridR[(x + i, y + j)] = 8
                    if dir in self.right[go]:
                        for xi, yi in self.right[go][dir]:
                        # xi, yi = self.right[self.directionfrom[(i, j)]]
                            if 0 <= x + i + xi < self.height and 0 <= y + j + yi < self.width and self.countgridR[
                                (x + i + xi, y + j + yi)] != 8:
                                self.countgridR[(x + i + xi, y + j + yi)] = 1

                    self.countgridL[(x + i, y + j)] = 8
                    if dir in self.left[go]:
                        for xi, yi in self.left[go][dir]:
                            # xi, yi = self.left[self.directionfrom[(i, j)]]
                            if 0 <= x + i + xi < self.height and 0 <= y + j + yi < self.width and self.countgridL[
                                (x + i + xi, y + j + yi)] != 8:
                                self.countgridL[(x + i + xi, y + j + yi)] = 1

        L = np.count_nonzero(self.countgridL == 1)
        R = np.count_nonzero(self.countgridR == 1)
        if L > R:
            return self.fill_holes(self.countgridR)
        else:
            return self.fill_holes(self.countgridL)

    def fill_holes(self, matrix):
        checkX = list(np.where(matrix == 1)[0])
        checkY = list(np.where(matrix == 1)[1])
        adjacent = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        while len(checkX) != 0:
            x = checkX.pop(0)
            y = checkY.pop(0)
            for i, j in adjacent:
                if 0 <= x + i < self.height and 0 <= y + j < self.width and matrix[(x + i, y + j)] == 0:
                    matrix[(x + i, y + j)] = 1
                    checkX.append(x + i)
                    checkY.append(y + j)

        for row in matrix:
            print("".join("■" if cell == 1 else "O" if cell == 8 else "." for cell in row))

        return np.count_nonzero(matrix == 1)


with open('2023-10-Pipe-Maze.txt') as f:
    lines = f.read().splitlines()
    # print(lines)

Maze = Grid(lines)
print("Part 1, the farthest step of the loop is", Maze.walk())
print("Part 2, the number of inner loops", Maze.inner())
