import numpy as np


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array([list(row) for row in lines])

    def collide_with_trees(self, dx, dy):
        x, y = 0, 0
        trees = 0
        while y < self.height:
            if self.grid[y][x] == "#": trees += 1
            y += dy
            x = (x + dx) % self.width
        return trees


with open('2020-03-Toboggan_Trajectory.txt') as f:
    lines = f.read().splitlines()
    Trajectory = Grid(lines)

    print("Part 1, numbers of trees is", Trajectory.collide_with_trees(3, 1))

    multiplication = (Trajectory.collide_with_trees(1, 1) *
                      Trajectory.collide_with_trees(3, 1) *
                      Trajectory.collide_with_trees(5, 1) *
                      Trajectory.collide_with_trees(7, 1) *
                      Trajectory.collide_with_trees(1, 2))

    print("Part 2, numbers of trees multiplied is", multiplication)
