import numpy as np
import heapq
class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = max(len(l) for l in lines)
        self.map = np.zeros((self.height, self.width))
        self.makemap(lines)

        self.start = (0, 0)
        self.finish = (self.height - 1, self.width - 1)

        self.options = {(0, 1), (-1, 0), (1, 0), (0, -1)}
        self.cheapmap = np.full((self.height, self.width),9999)
        self.visited = np.zeros((self.height, self.width))


    def printgrid(self):
        for row in self.map:
            print(row)

    def makemap(self, lines):
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                self.map[i][j] = l

    def dijkstra(self,root):
        n = self.width * self.height
        x, y = root
        self.cheapmap[x][y] = 0
        pq = [(0, root)]
        while len(pq) > 0:
            dist, current = heapq.heappop(pq)
            x,y =current
            if self.visited[current] == 1:
                continue
            self.visited[current] = 1
            for i,j in self.options:
                if 0 <= x + i < self.height and 0 <= y + j < self.width:
                    if self.cheapmap[x][y] + self.map[x+i][y+j] < self.cheapmap[x+i][y+j]:
                        self.cheapmap[x+i][y+j] = self.cheapmap[x][y] + self.map[x+i][y+j]
                        heapq.heappush(pq, (self.cheapmap[x+i][y+j], (x+i,y+j)))

        print(self.cheapmap)
        return self.cheapmap[self.finish]

    def makebiggergrid(self):
        addv = np.ones((self.height, self.width))
        addh = np.ones((self.height, self.width*5))
        copymap = self.map.copy()
        for i in range(1,5):
            copymap += addv
            copymap[copymap == 10] = 1
            self.map = np.concatenate((self.map,copymap),axis=1)

        copymap = self.map.copy()
        for i in range(1,5):
            copymap += addh
            copymap[copymap == 10] = 1
            self.map = np.concatenate((self.map,copymap),axis=0)

        self.height *=5
        self.width *= 5
        self.finish = (self.height-1,self.width-1)
        self.cheapmap = np.full((self.height, self.width),99999)
        self.visited = np.zeros((self.height, self.width))
        return self.dijkstra(self.start)










with open('2021-15-Chiton.txt') as f:
    lines = f.read().splitlines()

cave = Grid(lines)
print("Part 1, lowest risk path contains a risk of: ", cave.dijkstra(cave.start))
print("Part 2, lowest risk path contains a risk of: ", cave.makebiggergrid())

