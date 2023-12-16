import numpy as np


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = [[c for c in row] for row in lines]

        self.lava = np.zeros((self.height, self.width))
        self.seen = set()
        self.mirror_dir = {'\\': {(0, 1): (1, 0), (1, 0): (0, 1), (0, -1): (-1, 0), (-1, 0): (0, -1)},
                           '/': {(0, 1): (-1, 0), (1, 0): (0, -1), (0, -1): (1, 0), (-1, 0): (0, 1)}}

    def printgrid(self):
        print("Floor:")
        for row in self.grid:
            print("".join(row))
        print("Lava")
        for row in self.lava:
            print("".join("■" if cell == 1 else "." for cell in row))

    def lava_tiles(self,start=(0, -1), direction=(0, 1)):
        self.lava = np.zeros((self.height, self.width))
        self.seen.clear()
        self.flow(start, direction)
        return np.count_nonzero(self.lava > 0)

    def best_tiles(self):
        answers = []
        for i in range(self.height):
            answers.append(self.lava_tiles((i,-1), (0,1)))
            answers.append(self.lava_tiles((i,self.width), (0,-1)))
        for i in range(self.width):
            answers.append(self.lava_tiles((-1,i), (1,0)))
            answers.append(self.lava_tiles((self.height,i), (-1,0)))
        return max(answers)


    def flow(self, start, direction):
        x, y = start
        xi, yi = direction
        while (0 <= x + xi < self.height and 0 <= y + yi < self.width):
            x += xi
            y += yi
            self.lava[x][y] = 1
            if self.grid[x][y] in self.mirror_dir.keys():
                if ((x,y),self.mirror_dir[self.grid[x][y]][direction]) in self.seen:
                    break
                self.seen.add(((x,y),self.mirror_dir[self.grid[x][y]][direction]))
                self.flow((x,y),self.mirror_dir[self.grid[x][y]][direction])
                break
            elif self.grid[x][y] == "-":
                if direction == (1,0) or direction == (-1,0):
                    if ((x,y),(0,1)) in self.seen:
                        break
                    self.seen.add(((x,y),(0,1)))
                    self.flow((x,y),(0,1))
                    self.flow((x,y),(0,-1))
                    break
            elif self.grid[x][y] == "|":
                if direction == (0,1) or direction == (0,-1):
                    if ((x,y),(1,0)) in self.seen:
                        break
                    self.seen.add(((x,y),(1,0)))
                    self.flow((x,y),(1,0))
                    self.flow((x,y),(-1,0))
                    break



with open('2023-16-Floor-is-lava.txt') as f:
    lines = f.read().splitlines()

floor = Grid(lines)
print("Part 1, the number of lava tiles are:", floor.lava_tiles())
print("Part 2, the number of lava tiles are:", floor.best_tiles())
