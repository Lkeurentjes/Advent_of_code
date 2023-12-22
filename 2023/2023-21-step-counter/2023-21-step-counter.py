import numpy as np
import sys
import time

sys.setrecursionlimit(10 ** 6)
np.seterr(divide='ignore', invalid='ignore')
from functools import cache, cached_property

from queue import PriorityQueue
import heapq


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


    def dijkstra(self, inf_grid, roots):
        pq = []
        for s in range(0, len(roots), 2):
            pq.append((roots[s], roots[s + 1]))
            inf_grid[roots[s + 1]] = roots[s]
        while len(pq) > 0:
            dist, current = heapq.heappop(pq)
            x, y = current
            for i, j in self.directions.values():
                if 0 <= x + i < self.height and 0 <= y + j < self.width and self.grid[x + i][y + j] != "#":
                    if inf_grid[x + i][y + j] > dist + 1:
                        inf_grid[x + i][y + j] = dist + 1
                        heapq.heappush(pq, (dist + 1, (x + i, y + j)))


    @cache  # remembers when part of line is already been in the function, so builds "knowledge" over time
    def check_grid(self, start):
        inf_grid = np.ones((self.height, self.width)) * np.inf
        self.dijkstra(inf_grid,start)
        t = list(np.unique(inf_grid))
        return t[-2], inf_grid


    def infinite_walk(self, maxsteps):
        sum_possible = 0
        visited = set()
        startG = (0, 0)
        Queue = PriorityQueue()
        Queue.put((0, (startG, (0, self.start))))
        while not Queue.empty():
            step, ((xg, yg), start) = Queue.get()
            # print(step, ((xg, yg), start))
            if (xg, yg) in visited:
                continue
            visited.add((xg, yg))
            most, grid = self.check_grid(start)

            if step + most < maxsteps:
                sum_possible += np.count_nonzero(grid % 2 == step % 2)
            else:
                find = maxsteps - step
                sum_possible += np.count_nonzero(np.logical_and(grid % 2 == step % 2, grid <= find))

            if min(grid[0]) + step < maxsteps:
                next = []
                for i in list(np.where(grid[0] + step < maxsteps)[0]):
                    next.append(grid[0][i] - min(grid[0]))
                    next.append((self.height - 1, i))
                Queue.put((min(grid[0]) + step + 1, ((xg, yg - 1), tuple(next))))

            if min(grid[-1]) + step < maxsteps:
                next = []
                for i in list(np.where(grid[-1] + step < maxsteps)[0]):
                    next.append(grid[-1][i] - min(grid[-1]))
                    next.append((0, i))
                Queue.put((min(grid[-1]) + step + 1, ((xg, yg + 1), tuple(next))))

            if min(grid[:, 0]) + step < maxsteps:
                next = []
                for i in list(np.where(grid[:, 0] + step < maxsteps)[0]):
                    next.append(grid[:, 0][i] - min(grid[:, 0]))
                    next.append((i, self.width - 1))
                Queue.put((min(grid[:, 0]) + step + 1, ((xg - 1, yg), tuple(next))))

            if min(grid[:, -1]) + step < maxsteps:
                next = []
                for i in list(np.where(grid[:, -1] + step < maxsteps)[0]):
                    next.append(grid[:, -1][i] - min(grid[:, -1]))
                    next.append((i, 0))
                Queue.put((min(grid[:, -1]) + step + 1, ((xg + 1, yg), tuple(next))))

            # print(grid)
        return sum_possible


with open('2023-21-step-counter.txt') as f:
    lines = f.read().splitlines()
Garden = Grid(lines)
print("Part 1, 64 steps can reach this number of plots: ", Garden.walk(64))
start_time = time.time()
print("Part 2, x steps can reach this number of plots: ", Garden.infinite_walk(26501365))
print("--- %s seconds ---" % (time.time() - start_time))
# print("Part 2, x steps can reach this number of plots: ", Garden.infinite_walk(26501365))
