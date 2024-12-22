import numpy as np
from collections import deque
from scipy.ndimage import label

class Grid:
    def __init__(self, obstacles, height, width):
        """Initialize the grid with obstacles and dimensions."""
        self.height = height
        self.width = width
        self.grid = np.zeros((height, width), dtype=int)

        for x, y in obstacles:
            self.grid[y][x] = 1  # Mark obstacle positions as 1

        self.start = (0, 0)  # Top-left corner
        self.end = (height - 1, width - 1)  # Bottom-right corner

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right

    def is_safe(self, x, y):
        """Check if a cell is safe to enter."""
        return 0 <= x < self.height and 0 <= y < self.width and self.grid[x][y] == 0

    def bfs_shortest_path(self):
        """Find the shortest path from start to end using BFS."""
        queue = deque([(self.start, 0)])  # (current_position, steps_taken)
        visited = {self.start}

        while queue:
            (x, y), steps = queue.popleft()

            if (x, y) == self.end:
                return steps  # Return steps when the end is reached

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if self.is_safe(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

        return -1  # Return -1 if there's no path

def find_disconnection_step(obstacles, height, width):
    """Find the step where the path to the exit becomes impossible."""
    grid = np.zeros((height, width), dtype=int)
    structure = np.array([[0, 1, 0],
                          [1, 1, 1],
                          [0, 1, 0]])  # 4-connectivity mask

    for i, (x, y) in enumerate(obstacles):
        grid[y][x] = 1
        zero_mask = (grid == 0)

        # Label connected components in the grid
        labeled_grid, num_components = label(zero_mask, structure=structure)

        # Skip further checks if there is only one component
        if num_components == 1:
            continue

        # Check if start and end are still in the same connected component
        if labeled_grid[0, 0] != labeled_grid[height - 1, width - 1]:
            return i, (x, y)

    return -1, None  # Return -1 if the path remains connected

if __name__ == "__main__":
    with open('2024-18-RAM_Run.txt') as file:
        obstacles = [tuple(map(int, line.split(','))) for line in file.read().splitlines()]

    # Initialize grid dimensions and simulate the problem
    grid_height, grid_width, max_bytes = 71, 71, 1024
    memory = Grid(obstacles[:max_bytes], grid_height, grid_width)

    # Part 1: Minimum steps to reach the exit
    min_steps = memory.bfs_shortest_path()
    print("Part 1, the minimum steps to reach the exit:", min_steps)

    # Part 2: Step when the path becomes impossible
    step, coord = find_disconnection_step(obstacles, grid_height, grid_width)
    print("Part 2, the memory after path becomes impossible at step:", step, "is coordinate:", coord)
