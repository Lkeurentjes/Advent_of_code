import numpy as np
import sys
sys.setrecursionlimit(10**6)
np.seterr(divide='ignore', invalid='ignore')
from functools import cache, cached_property

from queue import PriorityQueue


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array([[c for c in row] for row in lines])
        self.stepgrid = np.ones((self.height, self.width)) * np.inf
        self.start = (list(np.where(self.grid == "S")[0])[0], list(np.where(self.grid == "S")[1])[0])
        self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def printgrid(self):
        print("garden")
        for row in self.grid:
            print("".join("■" if cell == "#" else "." for cell in row))
        print("steps")
        print(self.stepgrid)

    def make_step_grid(self, step, current, max):
        x, y = current
        if self.grid[x][y] != "#":
            if step < self.stepgrid[x][y] and step <= max:
                self.stepgrid[x][y] = step
                for i, j in self.directions.values():
                    if 0 <= x + i < self.height and 0 <= y + j < self.width:
                        self.make_step_grid(step + 1, (x + i, y + j), max)

    def walk(self, steps):
        self.make_step_grid(0, self.start, steps)
        # self.printgrid()
        even = steps % 2
        return np.count_nonzero(self.stepgrid % 2 == even)

    # @cached_property
    def fill_grid(self, in_grid, step, current):
        x, y = current
        if self.grid[x][y] != "#":
            if step < in_grid[x][y]:
                in_grid[x][y] = step
                for i, j in self.directions.values():
                    if 0 <= x + i < self.height and 0 <= y + j < self.width:
                        self.fill_grid(in_grid, step + 1, (x + i, y + j))

    @cache  # remembers when part of line is already been in the function, so builds "knowledge" over time
    def check_grid(self, start):
        inf_grid = np.ones((self.height, self.width)) * np.inf
        for s in range(0, len(start), 2):
            # print(start[s], start[s + 1])
            self.fill_grid(inf_grid, start[s], start[s + 1])
        t = list(np.unique(inf_grid))
        return t[-2], inf_grid

    def make_bigger_grid(self, times):
        self.grid = np.tile(self.grid, (times, times))
        self.height *= times
        self.width *= times
    def infinite_walk(self, maxsteps):
        sum_possible = 0
        self.make_bigger_grid(1)
        Max_boxes_h = maxsteps // (self.height // 2) * 2 - 1
        Max_boxes_v = maxsteps // (self.width // 2) * 2 - 1
        startgrid = (Max_boxes_h // 2, Max_boxes_v // 2)
        massivecheckgrid = np.zeros((Max_boxes_v, Max_boxes_h))
        Queue = PriorityQueue()
        Queue.put((0, (startgrid, (0, self.start))))
        while not Queue.empty():
            step, ((xg, yg), start) = Queue.get()
            print(step, ((xg, yg), start))
            if massivecheckgrid[xg][yg] == 1:
                continue
            massivecheckgrid[xg][yg] = 1
            most, grid = self.check_grid(start)
            # print("\n")
            # print(step, most, maxsteps)

            if step + most < maxsteps:
                sum_possible += np.count_nonzero(grid % 2 == step % 2)
            else:
                find = maxsteps - step
                sum_possible += np.count_nonzero(np.logical_and(grid % 2 == step % 2, grid <= find))

            if min(grid[0]) + step < maxsteps:
                # print(list(np.where(grid[0] + step < maxsteps)[0]))
                next = []
                for i in list(np.where(grid[0] + step < maxsteps)[0]):
                    next.append(grid[0][i] - min(grid[0]))
                    next.append((self.height - 1, i))
                Queue.put((min(grid[0])+ step + 1, ((xg, yg - 1), tuple(next))))

            if min(grid[-1]) + step < maxsteps:
                next = []
                for i in list(np.where(grid[-1] + step < maxsteps)[0]):
                    next.append(grid[-1][i] - min(grid[-1]))
                    next.append((0, i))
                Queue.put((min(grid[-1])+ step + 1, ((xg, yg + 1), tuple(next))))

            if min(grid[:, 0]) + step < maxsteps:
                # print(list(np.where(grid[0] + step < maxsteps)[0]))
                next = []
                for i in list(np.where(grid[:, 0] + step < maxsteps)[0]):
                    next.append(grid[:, 0][i] - min(grid[:, 0]))
                    next.append((i, self.width - 1))
                Queue.put((min(grid[:,0])+ step + 1, ((xg - 1, yg), tuple(next))))

            if min(grid[:, -1]) + step < maxsteps:
                # print(list(np.where(grid[0] + step < maxsteps)[0]))
                next = []
                for i in list(np.where(grid[:, -1] + step < maxsteps)[0]):
                    next.append(grid[:, -1][i] - min(grid[:, -1]))
                    next.append((i, 0))
                Queue.put((min(grid[:,-1]) + step + 1, ((xg + 1, yg), tuple(next))))


            # print(grid)
        return sum_possible


with open('2023-21-step-counter.txt') as f:
    lines = f.read().splitlines()
Garden = Grid(lines)
print("Part 1, 64 steps can reach this number of plots: ", Garden.walk(64))
# print("Part 1, 16 steps can reach this number of plots: ", Garden.walk(16))
print("Part 2, x steps can reach this number of plots: ", Garden.infinite_walk(5000))
