import numpy as np


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array(lines)

        self.directions = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1),  # right
            (-1, -1),  # up-left
            (-1, 1),  # up-right
            (1, -1),  # down-left
            (1, 1)  # down-right
        ]

    def on_map(self, x, y):
        # check if x, y coord exist
        return 0 <= x < self.height and 0 <= y < self.width

    def get_neighbors(self, x, y):
        # get the neighbours that exist
        neighbors = []
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.on_map(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def active_neighbours(self, x, y):
        neighbors = self.get_neighbors(x, y)
        active_neighbors = sum(self.grid[nx, ny] for nx, ny in neighbors)
        return active_neighbors

    def analyze_neighbors(self):
        less_than_4_count = 0
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x, y] == 1:  # Only check cells that are 1
                    if self.active_neighbours(x, y) < 4:
                        less_than_4_count += 1
        return less_than_4_count

    def clean(self):
        cleancount = 0
        while True:
            changeGrid = []
            for x in range(self.height):
                for y in range(self.width):
                    if self.grid[x, y] == 1:  # Only check cells that are 1
                        if self.active_neighbours(x, y) < 4:
                            cleancount += 1
                            changeGrid.append((x, y))
            if changeGrid:
                for x, y in changeGrid:
                    self.grid[x, y] = 0
            else:
                return cleancount


with open('2025-04-PrintingDepartment.txt') as f:
    lines = [[1 if i == "@" else 0 for i in row] for row in f.read().splitlines()]
    map = Grid(lines)
    print(f"Part 1, Cells with <4 active neighbors: {map.analyze_neighbors()}")
    print(f"Part 2, Total cells to clean: {map.clean()}")
