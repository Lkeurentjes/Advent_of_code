import numpy as np
class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array([[1 if cell == '#' else 0 for cell in row] for row in lines])

    def printgrid(self):
        for row in self.grid:
            print("".join("■" if cell > 0 else "." for cell in row))

    def reflection_sum(self):
        h_reflection = self.h_reflection()
        return 100 * h_reflection if h_reflection is not None else self.v_reflection()


    def v_reflection(self):
        for col in range(self.width):
            for other_col in range(col+1,self.width,2):
                half = (other_col - col)//2
                if np.array_equal(self.grid[:, col: col +half+1], np.flip(self.grid[:,other_col-half:other_col+1], axis=1)):
                    if col== 0 or other_col == self.width-1:
                        return (col+other_col+1)//2
        return None

    def h_reflection(self):
        for row in range(self.height):
            for other_row in range(row+1,self.height,2):
                half = (other_row - row)//2
                if np.array_equal(self.grid[row: row +half+1], np.flip(self.grid[other_row-half:other_row+1], axis=0)):
                    if row == 0 or other_row == self.height-1:
                        return (row+other_row+1)//2
        return None

    def smudge_sum(self):
        h_reflection = self.h_smudge_reflection()
        return 100 * h_reflection if h_reflection is not None else self.v_smudge_reflection()

    def h_smudge_reflection(self):
        for row in range(self.height):
            for other_row in range(row+1,self.height,2):
                half = (other_row - row)//2
                new_array = self.grid[row: row +half+1] + np.flip(self.grid[other_row-half:other_row+1], axis=0)
                if np.count_nonzero(new_array == 1) == 1:
                    if row == 0 or other_row == self.height-1:
                        return (row+other_row+1)//2
        return None

    def v_smudge_reflection(self):
        for col in range(self.width):
            for other_col in range(col+1,self.width,2):
                half = (other_col - col)//2
                new_array = self.grid[:, col: col +half+1] + np.flip(self.grid[:,other_col-half:other_col+1], axis=1)
                if np.count_nonzero(new_array == 1) == 1:
                    if col== 0 or other_col == self.width-1:
                        return (col+other_col+1)//2
        return None

with open('2023-13-Point-of-Incidence.txt') as f:
    lines = f.read().split("\n\n")
    grids = [line.split("\n") for line in lines]

ref_sum, smudge_sum = 0, 0
for grid in grids:
    ground = Grid(grid)
    # ground.printgrid()
    ref_sum += ground.reflection_sum()
    smudge_sum += ground.smudge_sum()

print("part 1, reflection sum is", ref_sum)
print("part 2, smudge sum is", smudge_sum)

