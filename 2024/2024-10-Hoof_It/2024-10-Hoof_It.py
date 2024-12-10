import numpy as np
from collections import deque

class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array(lines)

        self.starts = np.argwhere(self.grid == 0) # start at zero locations

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # directions: up, down, left, right

    def on_map(self,x,y):
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

    def find_trailheads(self):
        scores = []

        for x, y in self.starts:
            # BFS to get scores
            queue = deque([(x, y)])
            visited = set()
            reachable_finish = set()

            while queue:
                x,y = queue.popleft()

                if (x, y) in visited:
                    continue
                visited.add((x, y))

                if self.grid[x, y] == 9:
                    reachable_finish.add((x, y))
                    continue

                for nx, ny in self.get_neighbors(x, y):
                    if (nx, ny) not in visited and self.grid[nx, ny] == self.grid[x, y] + 1:
                        queue.append((nx, ny))

            # add numbers 9 that are reachable
            scores.append(len(reachable_finish))

        return scores

    def find_ratings(self):
        ratings = []

        for x, y in self.starts:
            # BFS to get rating
            queue = deque([(x, y)])
            trail_counts = {}
            trail_counts[(x, y)] = 1

            while queue:
                x, y = queue.popleft()

                for nx, ny in self.get_neighbors(x, y):
                    if self.grid[nx, ny] == self.grid[x, y] + 1:
                        if (nx, ny) not in trail_counts:
                            queue.append((nx, ny))
                        trail_counts[(nx, ny)] = trail_counts.get((nx, ny), 0) + trail_counts[(x, y)]

            # add sum of ways to get to 9
            ratings.append(sum(val for (x, y), val in trail_counts.items() if self.grid[x, y] == 9))
        return ratings


with open('2024-10-Hoof_It.txt') as f:
    lines = [[int(i)for i in row]for row in f.read().splitlines()]
    map = Grid(lines)
    print("Part 1, sum of scores",sum(map.find_trailheads()))
    print("Part 2, sum of ratings",sum(map.find_ratings()))

