import numpy as np
from collections import deque


class Grid:
    def __init__(self, lines):
        self.alist = []
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                # print(lines[i][j])
                if lines[i][j] == "S":
                    self.start = (i, j)
                    self.alist.append((i, j))
                    row.append(1)
                elif lines[i][j] == "E":
                    self.finish = (i, j)
                    row.append(26)
                else:
                    if lines[i][j] == "a":
                        self.alist.append((i,j))
                    row.append(ord(lines[i][j]) - 96)
            self.grid.append(row)
        # print(self.grid, self.start, self.finish)
        self.visited = np.zeros((self.height, self.width))
        self.dist = {self.start:0}

        self.pathlength = self.width*self.height



    def bfs_path(self, position, positionheight, distance):
        delta_x = [-1, 1, 0, 0]
        delta_y = [0, 0, 1, -1]
        Q = deque([position])
        self.dist = {position: 0}
        while len(Q):
            # print(Q)
            curPoint = Q.popleft()
            curDist = self.dist[curPoint]
            if curPoint == self.finish:
                # print(self.dist)
                return curDist
            for dx, dy in zip(delta_x, delta_y):
                nextPoint = (curPoint[0] + dx, curPoint[1] + dy)
                height = self.grid[curPoint[0]][curPoint[1]]
                if self.can_visit(nextPoint[0],nextPoint[1],height):
                    self.dist[nextPoint] = curDist + 1
                    Q.append(nextPoint)
                else:
                    continue


    def can_visit(self, x, y, startheight):
        return (x >= 0 and x < self.height and y >= 0 and y < self.width and self.grid[x][y] - startheight <= 1 and (x,y) not in self.dist.keys())
                #andself.visited[x][y] >= 0)


with open('2022-12Path-finding.txt') as f:
    lines = f.read().splitlines()
    landscape = Grid(lines)
    length = landscape.bfs_path(landscape.start, 1, 0)
    print("PART 1: The shortest route from the start is",length, "steps")
    # print(landscape.alist)
    minlength = landscape.height*landscape.width
    for a in landscape.alist:
        length = landscape.bfs_path(a, 1, 0)
        # print(length)
        if length is not None:
            if length < minlength:
                minlength = length
    print("PART 1: The shortest route from an elavation a is",minlength, "steps")


