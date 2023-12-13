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

    def printgrid(self):
        for row in self.grid:
            print("".join("■" if cell > 0 else "." for cell in row))

    def reflection_sum(self):
        h_reflection = self.h_reflection()
        if h_reflection is not None:
            return 100 * h_reflection
        v_reflection = self.v_reflection()
        if v_reflection is not None:
            return v_reflection
        return 0

    def v_reflection(self):
        mirror = []
        for col in range(self.width):
            for other_col in range(col+1,self.width,2):
                half = (other_col - col)//2
                if np.array_equal(self.grid[:, col: col +half+1], np.flip(self.grid[:,other_col-half:other_col+1], axis=1)):
                    if col== 0 or other_col == self.width-1:
                        print("v",col, other_col, (col+other_col+1)//2)
                        mirror.append((col+other_col+1)//2)
        if len(mirror) != 0:
            return max(mirror)
        return None

    def h_reflection(self):
        mirror = []
        for row in range(self.height):
            for other_row in range(row+1,self.height,2):
                half = (other_row - row)//2
                if np.array_equal(self.grid[row: row +half+1], np.flip(self.grid[other_row-half:other_row+1], axis=0)):
                    if row == 0 or other_row == self.height-1:
                        print("h",row, other_row, (row+other_row+1)//2)
                        mirror.append((row+other_row+1)//2)
        if len(mirror) != 0:
            return max(mirror)
        return None

    def smudge_sum(self):
        h_reflection = self.h_smudge_reflection()
        v_reflection = self.v_smudge_reflection()

        if h_reflection is not None:
            return 100 * h_reflection

        if v_reflection is not None:
            return v_reflection
        return 0

    def h_smudge_reflection(self):
        mirror = []
        for row in range(self.height):
            for other_row in range(row+1,self.height,2):
                half = (other_row - row)//2
                if np.array_equal(self.grid[row: row +half+1], np.flip(self.grid[other_row-half:other_row+1], axis=0)):
                    if row == 0 or other_row == self.height-1:
                        print("h",row, other_row, (row+other_row+1)//2)
                        mirror.append((row+other_row+1)//2)
        if len(mirror) != 0:
            return max(mirror)
        return None

    def v_smudge_reflection(self):
        a=1

with open('2023-13-Point-of-Incidence.txt') as f:
    lines = f.read().split("\n\n")
    grids = [line.split("\n") for line in lines]
    print(grids)

ref_sum = 0
for grid in grids:
    ground = Grid(grid)
    ground.printgrid()
    ref_sum += ground.reflection_sum()

print("part 1, reflection sum is", ref_sum)

