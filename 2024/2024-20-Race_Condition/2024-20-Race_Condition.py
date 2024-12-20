import numpy as np
import heapq
from itertools import product


class Grid:
    def __init__(self, lines):
        self.grid = np.array([list(row) for row in lines])
        self.height, self.width = self.grid.shape

        self.start = tuple(np.argwhere(self.grid == 'S')[0])
        self.end = tuple(np.argwhere(self.grid == 'E')[0])

        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
        self.cheapmap = np.full((self.height, self.width), np.inf)

    def is_valid(self, r, c):
        return 0 <= r < self.height and 0 <= c < self.width

    def dijkstra(self):
        # Dijkstra's algorithm to calculate the shortest path from the start
        x, y = self.start
        self.cheapmap[x][y] = 0
        pq = [(0, (x, y))]

        while pq:
            sec, (x, y) = heapq.heappop(pq)

            # Skip if a shorter path to this cell has already been found
            if sec > self.cheapmap[x][y]:
                continue

            for dx, dy in self.directions:
                newx, newy = x + dx, y + dy
                newsec = sec + 1
                if self.is_valid(newx, newy) and self.grid[newx, newy] != "#" and newsec < self.cheapmap[newx, newy]:
                    # Update the cost map and add the neighbor to the queue
                    self.cheapmap[newx, newy] = newsec
                    heapq.heappush(pq, (newsec, (newx, newy)))

    def calculate_cheats(self, min_cheat):
        # Calculate cheats where shortcuts are more than min cheat
        self.dijkstra()
        counter = 0

        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x, y] == "#":
                    # Get adjacent values
                    adjacent = []
                    for dx, dy in self.directions:
                        newx = x + dx
                        newy = y + dy
                        if self.is_valid(newx, newy) and not np.isinf(self.cheapmap[newx, newy]):
                            adjacent.append(self.cheapmap[newx, newy])

                    # If there are at least two reachable neighbors
                    if len(adjacent) >= 2:
                        max_diff = max(adjacent) - min(adjacent) - 2  # minus 2 for the two steps
                        if max_diff >= min_cheat:
                            counter += 1
        return counter

    def calculate_cheats_jumps(self, Maxjump, min_cheat):
        self.dijkstra()
        counter = 0

        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x, y] != "#":
                    # Explore all possible jumps within the Maxjump distance
                    for dx, dy in product(range(-Maxjump, Maxjump + 1), repeat=2):
                        steps = abs(dx) + abs(dy)
                        if dx == dy == 0 or steps > Maxjump:
                            continue
                        addx, addy = x + dx, y + dy
                        if self.is_valid(addx, addy) and not np.isinf(self.cheapmap[addx, addy]):
                            max_diff = self.cheapmap[addx, addy] - self.cheapmap[x, y] - steps
                            if max_diff >= min_cheat:
                                counter += 1

        return counter


with open('2024-20-Race_Condition.txt') as f:
    lines = f.read().splitlines()
    Maze = Grid(lines)
    print("Part 1, possible shortcut cheats are", Maze.calculate_cheats(100))
    print("Part 1, possible shortcut cheats are", Maze.calculate_cheats_jumps(2, 100))
    print("Part 2, possible shortcut cheats are", Maze.calculate_cheats_jumps(20, 100))
