import numpy as np
from collections import deque
from scipy.ndimage import label


class Grid:
    def __init__(self, lines, height, width):
        self.lines = lines
        self.height = height
        self.width = width
        self.grid = np.zeros((height, width), dtype=int)
        for x, y in lines:
            self.grid[y][x] = 1

        self.start = (0, 0)  # Start at the top-left corner
        self.end = (height - 1, width - 1)  # End at the bottom-right corner

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right

    def is_safe(self, x, y):
        # Check if a cell is not corrupted
        return 0 <= x < self.height and 0 <= y < self.width and self.grid[x][y] == 0

    def bfs_shortest_path(self):
        # BFS to find the shortest path from start to end
        queue = deque([(self.start, 0)])  # (current_position, steps_taken)
        visited = {self.start}

        while queue:
            (x, y), steps = queue.popleft()

            if (x, y) == self.end:
                return steps  # Return the number of steps when the end is reached

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_safe(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

        return -1  # Return -1 if there's no path


def find_connected_components(lines, height, width):
    grid = np.zeros((height, width), dtype=int)

    # 4 connectivity mask
    structure = np.array([[0, 1, 0],
                          [1, 1, 1],
                          [0, 1, 0]])

    for i, (x, y) in enumerate(lines):
        grid[y][x] = 1
        zero_mask = (grid == 0)

        # Use the mask to label connected components in the grid
        labeled_grid, num_components = label(zero_mask, structure=structure)

        # skip further checks
        if num_components == 1:
            continue

        # check is start and end are still in the same connected component
        if labeled_grid[0, 0] != labeled_grid[height - 1, width - 1]:
            return i, (x, y)


with open('2024-18-RAM_Run.txt') as f:
    lines = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

    # Initialize grid size and simulate the problem
    # grid_height, grid_width, input = 7, 7, 12  #  Example grid
    grid_height, grid_width, input = 71, 71, 1024  # Assuming the 71x71 grid and only first 1024
    Memory = Grid(lines[:input], grid_height, grid_width)

    print("Part 1, the minimum steps to reach the exit:", Memory.bfs_shortest_path())
    step, coord = find_connected_components(lines, grid_height, grid_width)
    print("Part 2, the memory after path comes impossible at step:", step, "is coordinate:", coord)
