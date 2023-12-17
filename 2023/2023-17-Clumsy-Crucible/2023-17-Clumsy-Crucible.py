import numpy as np
import heapq

class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = max(len(l) for l in lines)
        self.map = np.array([[int(ch) for ch in line.ljust(self.width)] for line in lines])

        self.options = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.cheapmap = np.full((self.height, self.width), np.inf)

    def printgrid(self):
        for row in self.map:
            print(row)

    def dijkstra(self, root, flowmin = 1 ,flowmax = 3):
        self.cheapmap.fill(np.inf)
        x, y = root
        self.cheapmap[x][y] = 0
        pq = [(0, root, (0, 0))]
        seen = set()

        while pq:
            heat, (x, y), (oldi, oldj) = heapq.heappop(pq)
            if ((x,y,oldi,oldj) in seen):
                continue
            seen.add((x,y,oldi,oldj))

            for i, j in self.options:
                heatnow = heat
                if (i == oldi and j == oldj) or (i == -oldi and j == -oldj):
                    # not olf direction or turn around
                    continue
                if 0 <= x + (i * (flowmin-1)) < self.height and 0 <= y + (j * (flowmin-1)) < self.width:
                    for h in range(1,flowmin):
                        xnew, ynew = x + (i * h), y + (j * h)
                        heatnow += self.map[xnew][ynew]

                for flow in range(flowmin, flowmax + 1):
                    xnew, ynew = x + (i * flow), y + (j * flow)
                    if 0 <= xnew < self.height and 0 <= ynew < self.width:
                        heatnow += self.map[xnew][ynew]
                        if heatnow < self.cheapmap[xnew][ynew]:
                            self.cheapmap[xnew][ynew] = heatnow
                        heapq.heappush(pq, (heatnow, (xnew, ynew), (i, j)))
                    else:
                        break

        return int(self.cheapmap[(-1, -1)])


with open('2023-17-Clumsy-Crucible.txt') as f:
    lines = f.read().splitlines()

City = Grid(lines)
print("Part 1, the shortest path is", City.dijkstra((0,0)))
print("Part 2, the shortest path is", City.dijkstra((0,0), 4, 10))
