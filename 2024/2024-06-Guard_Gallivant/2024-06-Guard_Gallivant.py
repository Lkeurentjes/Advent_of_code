import numpy as np
import sys
from collections import deque


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])

        self.start = [0, 0]
        self.obstacles = []
        for i in range(self.height):
            for j in range(self.width):
                if lines[i][j] == '#':
                    self.obstacles.append((i, j))
                if lines[i][j] == '^':
                    self.start = (i, j)

        self.pos = self.start

        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.dir = 0

        self.visited = set()

        self.check = 0

    def on_map(self, x, y):
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return False
        return True

    def turn(self):
        self.dir = (self.dir + 1) % 4

    def step(self, dx, dy):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def walk(self):
        #walk algorithm
        while self.on_map(self.pos[0], self.pos[1]):
            self.visited.add(self.pos)

            dx, dy = self.directions[self.dir]
            # turn if needed
            while (self.pos[0] + dx, self.pos[1] + dy) in self.obstacles:
                self.turn()
                dx, dy = self.directions[self.dir]
            # step
            self.step(dx, dy)

        return len(self.visited)


    def check_loop(self, pos, dir, obstacle):
        # check for loops based on "states" with same walk algorithm as part 1
        self.check += 1
        print(self.check)

        check_states = set()

        while self.on_map(pos[0], pos[1]):
            check_states.add((pos, dir))
            dx, dy = self.directions[dir]

            # turn if needed
            while (pos[0] + dx, pos[1] + dy) in self.obstacles or (pos[0] + dx, pos[1] + dy) == obstacle:
                dir = (dir + 1) % 4
                dx, dy = self.directions[dir]

            if ((pos[0] + dx, pos[1] + dy), dir) in check_states:
                # Found loop
                return True

            # step
            pos = (pos[0] + dx, pos[1] + dy)

        return False


    def add_obstacles(self):
        obstacle_count = 0
        # check all visited if the make a loop path
        for obstacle in self.visited:
            if self.check_loop(self.start, 0, obstacle):
                obstacle_count += 1
        return obstacle_count


with open('2024-06-Guard_Gallivant.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    Guard = Grid(lines)
    print("Part 1, cells visited", Guard.walk())
    # print("Part 1", Guard.Ray_walk())
    print("Part 2, possible obstacles for loops", Guard.add_obstacles())
