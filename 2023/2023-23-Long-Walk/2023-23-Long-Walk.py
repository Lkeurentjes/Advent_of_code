import numpy as np
import sys
from queue import PriorityQueue

sys.setrecursionlimit(10 ** 6)


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = np.array([[c for c in row] for row in lines])
        self.directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
        self.printgrid()
        self.finish = (self.height - 1, self.width - 2)
        self.visited = dict()
        self.graph = self.make_graph()


    def printgrid(self):
        print("garden")
        for row in self.grid:
            print("".join("■" if cell == "#" else "." for cell in row))

    def find_fork(self, start):
        Queue = [start]
        length = 0
        been = []
        while Queue:
            x,y = Queue.pop(0)
            if (x,y) in been:
                continue
            been.append((x,y))
            to = []
            for i, j in self.directions.values():
                if 0 <= x + i < self.height and 0 <= y + j < self.width and self.grid[x+i][y+j] != "#" and (x +i,y+j) not in been:
                    to.append((x+i, y+j))
            if len(to) == 0:
                return 1,2,3
            if len(to) != 1:
                return length, to
            Queue.append(to[0])
            length += 1

    def make_graph(self):
        a=1


    def longest_path(self, current, visited=set(), dist=0, max_dist=0, slopes=True):
        x, y = current
        if self.grid[x][y] == "#" or current in visited:
            return 0

        if current == self.finish:
            print(max_dist, dist)
            return max(max_dist, dist)



        visited.add(current)
        # print(current, dist, max_dist, visited)
        for i, j in self.directions.values():
            if 0 <= x + i < self.height and 0 <= y + j < self.width:
                new = (x + i, y + j)
                if slopes and self.grid[x + i][y + j] in self.directions.keys():
                    # print("heeere")
                    k, l = self.directions[self.grid[x + i][y + j]]
                    max_dist = max(max_dist,
                                   self.longest_path((x + i + k, y + j + l), visited, dist + 2, max_dist, slopes))
                else:
                    max_dist = max(max_dist, self.longest_path((x + i, y + j), visited, dist + 1, max_dist, slopes))

        visited.remove(current)

        return max_dist

    def longest_path_memo(self, current, visited=set(), dist=0, max_dist=0, slopes=True):
        x, y = current
        if self.grid[x][y] == "#" or current in visited:
            return 0

        if current == self.finish:
            print(max_dist, dist)
            return max(max_dist, dist)

        check = self.visited.get(current, 0)
        if check !=0:
            for d, v in check:
                if visited.issubset(v):
                    return 0
                # if d < dist:
                #     return 0


        visited.add(current)
        # print(current, dist, max_dist, visited)
        for i, j in self.directions.values():
            if 0 <= x + i < self.height and 0 <= y + j < self.width:
                # self.visited.setdefault(current, []).append(((0, visited)))
                new = (x + i, y + j)
                if slopes and self.grid[x + i][y + j] in self.directions.keys():
                    # print("heeere")
                    k, l = self.directions[self.grid[x + i][y + j]]
                    max_dist = max(max_dist,
                                   self.longest_path((x + i + k, y + j + l), visited, dist + 2, max_dist, slopes))
                else:
                    max_dist = max(max_dist, self.longest_path((x + i, y + j), visited, dist + 1, max_dist, slopes))

        self.visited.setdefault(current, []).append(((max_dist, visited)))
        visited.remove(current)




        return max_dist

    # def longest_path_memo(self, current, dist=0, max_dist=0, slopes=True):
    #     Queue = PriorityQueue()
    #     Queue.put((dist, current, {0}))
    #     visited_far = dict()
    #     visited_how = dict()
    #     while not Queue.empty():
    #         # print(visited_far)
    #         dist, (x,y), visited = Queue.get()
    #         dist *= -1
    #         print(dist)
    #         if self.grid[x][y] == "#" or (x,y) in visited:
    #             continue
    #
    #         if dist > visited_far.get((x,y), [-1,0])[0] :
    #             visited_far[(x,y)] = (dist, list(visited)[-1])
    #         else:
    #             if visited_far.get((x,y), [-1,0])[1] == list(visited)[-1]:
    #                 continue
    #
    #         if (x,y) == self.finish:
    #             continue
    #
    #         visited.add((x,y))
    #         for i, j in self.directions.values():
    #             if 0 <= x + i < self.height and 0 <= y + j < self.width:
    #                 v_copy = visited.copy()
    #                 if slopes and self.grid[x + i][y + j] in self.directions.keys():
    #                     k, l = self.directions[self.grid[x + i][y + j]]
    #                     Queue.put((-(dist + 2),(x + i + k, y + j + l), v_copy))
    #                 else:
    #                     Queue.put((-(dist + 1), (x + i, y + j), v_copy))
    #
    #
    #     return visited_far[self.finish]






with open('2023-23-Long-Walk.txt') as f:
    lines = f.read().splitlines()
    print(lines)
Maze = Grid(lines)
print("Part 1, Longest path is:", Maze.longest_path((0, 1)))
input("Hit enter")
# print("Part 1.1, Longest path is:", Maze.longest_path_memo((0, 1)))
# input("Hit enter")
print("Part 2.1, Longest path is:", Maze.longest_path_memo((0, 1), slopes=False))
input("Hit enter")
# print("Part 2, Longest path is:", Maze.longest_path((0, 1), slopes=False))
# input("Hit enter")

