import numpy as np


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array([[1 if cell == '#' else 2 if cell == "O" else 0 for cell in row] for row in lines])

    def printgrid(self):
        for row in self.grid:
            print("".join("■" if cell == 1 else "O" if cell == 2 else "." for cell in row))

    def totalload(self):
        self.roll()
        total_load = sum((self.height - x) for x in range(self.width) for y in range(self.height) if self.grid[x][y] == 2)
        return total_load
    def cycleload(self, times):
        seen, load = {}, {}
        #find where it cycles
        for i in range(1,times+1):
            for t in range(4):
                self.roll()
                self.grid = np.rot90(self.grid,3)

            current = self.grid.tobytes()
            if current in seen.keys() or i == times-1:
                break
            total_load = sum((self.height - x) for x in range(self.width) for y in range(self.height) if self.grid[x][y] == 2)
            seen[current] = i
            load[i] = total_load

        cyclelength = i - seen[current]
        index = seen[current] + (times - seen[current]) % cyclelength
        return load[index]

    def roll(self):
        for y in range(self.width):
            for x in range(self.height):
                if self.grid[x][y] == 2:
                    # move up as far as possible
                    x -= 1
                    while (x >= 0 and self.grid[x][y] == 0):
                        self.grid[x][y], self.grid[x+1][y] = self.grid[x+1][y], self.grid[x][y]
                        x-=1


with open('2023-14-Reflector-Dish.txt') as f:
    lines = f.read().splitlines()

Dish = Grid(lines)

print("Part 1, load after roll is", Dish.totalload())
print("Part 2, load after roll is", Dish.cycleload(1000000000))
