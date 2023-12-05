import numpy as np
import collections
from collections import deque

class Grid:
    def __init__(self, lines):
        self.faces = ["U", "R", "D", "L"]
        self.height = len(lines)
        self.width = max(len(l) for l in lines)
        self.map = np.zeros((self.height, self.width))
        self.makemap(lines)
        self.position = (0, np.where(self.map[0] == 1)[0][0])
        self.face = "R"

    def makemap(self, lines):
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                if l == ".":
                    self.map[i][j] = 1
                if l == "#":
                    self.map[i][j] = 9

    def Route(self, route):
        routelist = route.replace("R", " R ").replace("L", " L ").split()
        for r in routelist:
            if r.isdigit():
                self.Walk(int(r))
            else:
                self.Turn(r)
        return self.position, self.face

    def Walk(self, steps):
        for s in range(steps):
            x, y = self.position
            if self.face == "R":
                y = (y + 1) % self.width
                if self.map[x, y] == 0:
                    y = np.where(self.map[x] != 0)[0][0]
            if self.face == "L":
                y = (y - 1 + self.width) % self.width
                if self.map[x, y] == 0:
                    y = np.where(self.map[x] != 0)[0][-1]
            if self.face == "D":
                x = (x + 1) % self.height
                if self.map[x, y] == 0:
                    x = np.where(self.map[:, y] != 0)[0][0]
            if self.face == "U":
                x = (x - 1 + self.height) % self.height
                if self.map[x, y] == 0:
                    x = np.where(self.map[:, y] != 0)[0][-1]

            if self.map[x, y] == 9:
                break

            self.position = (x, y)

    def Turn(self, direction):
        index = self.faces.index(self.face)
        if direction == "R":
            self.face = self.faces[(index + 1) % 4]
        if direction == "L":
            self.face = self.faces[(index - 1) % 4]


class Cube:
    def __init__(self, lines):
        self.faces = ["U", "R", "D", "L"]
        self.adjacentedge = {"U": ["R", "L"], "R": ["D", "U"], "D": ["L", "R"], "L": ["U", "D"]}
        self.mirrordict = {"D": "U", "R": "L", "U": "D", "L": "R"}

        # flat part
        self.heightflat = len(lines)
        self.widthflat = max(len(l) for l in lines)
        self.flatmap = np.zeros((self.heightflat, self.widthflat))
        self.makemap(lines)

        # to cube
        self.squaresize = abs(self.heightflat - self.widthflat)
        self.minifold = self.make_mini_fold()
        self.connection = {}
        self.make_connections()

        print(self.connection)
        print(self.minifold)

        # start place
        self.position = (0, np.where(self.flatmap[0] == 1)[0][0])
        self.face = "R"

    def makemap(self, lines):
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                if l == ".":
                    self.flatmap[i][j] = 1
                if l == "#":
                    self.flatmap[i][j] = 9

    def make_mini_fold(self):
        heigth = self.heightflat // self.squaresize
        width = self.widthflat // self.squaresize
        mini = np.zeros((heigth, width))
        index = 1
        for i in range(heigth):
            for j in range(width):
                if self.flatmap[i * self.squaresize][j * self.squaresize] != 0:
                    mini[i][j] = index
                    index += 1
        return mini

    def make_connections(self):
        heigth = self.heightflat // self.squaresize
        width = self.widthflat // self.squaresize
        neigbourdict = {"D": (1, 0), "R": (0, 1), "U": (-1, 0), "L": (0, -1)}
        turndict = {i: {} for i in range(1, 7)}  # transitions

        edges_todo = set()
        edges_todo = deque(edges_todo)
        for i in range(heigth):
            for j in range(width):
                if self.minifold[i][j] != 0:
                    for key, value in neigbourdict.items():
                        x, y = value
                        X = (i + x + heigth) % heigth
                        Y = (j + y + width) % width
                        if self.minifold[X][Y] != 0:
                            # edges_todo.add((self.minifold[i][j], self.minifold[X][Y], key, 0))
                            edges_todo.append((self.minifold[i][j], self.minifold[X][Y], key, 0))


        # edges_todo = deque(edges_todo)
        while edges_todo:

            # face, to, direction, rotation = edges_todo.pop()
            face, to, direction, rotation = edges_todo.popleft()
            print("Adding this edge \t", face, to, direction, rotation)

            if direction in turndict[face]:
                continue
            turndict[face][direction] = (to, rotation)

            if len(turndict[to]) != 0:
                rotated_direction = self.faces[(self.faces.index(direction) + rotation) % 4]

                for check in self.adjacentedge[rotated_direction]:
                    if check in turndict[to]:
                        link, d = turndict[to][check]

                        dir_fl = self.faces[(self.faces.index(check) + rotation) % 4]
                        dir_lf = self.faces[(self.faces.index(direction) - rotation - d + 2) % 4]

                        turn_lf = (self.faces.index(dir_lf) - self.faces.index(dir_fl) + 4 + 2) % 4
                        turn_fl = (self.faces.index(dir_fl) - self.faces.index(dir_lf) + 4 + 2) % 4

                        # print("\t **CHECK IS FOUND**")
                        # print("\t\t\t\t", (face, link, dir_fl, turn_fl))
                        # print("\t\t\t\t", (link, face, dir_lf, turn_lf))

                        # edges_todo.add((face, link, dir_fl, turn_fl))
                        # edges_todo.add((link, face, dir_lf, turn_lf))

                        edges_todo.append((face, link, dir_fl, turn_fl))
                        edges_todo.append((link, face, dir_lf, turn_lf))




        print(self.minifold)
        print("Connectionsmade")
        for key, value in turndict.items():
            print(key, sorted(value.items()))

    def Route(self, route):
        routelist = route.replace("R", " R ").replace("L", " L ").split()
        for r in routelist:
            if r.isdigit():
                self.Walk(int(r))
            else:
                self.Fold_turn(r)
        return self.position, self.face

    def Walk(self, steps):
        for s in range(steps):
            x, y = self.position
            if self.face == "R":
                y = (y + 1)
                if y == self.width:
                    a = 1
            if self.face == "L":
                y = (y - 1 + self.width) % self.width
                if self.flatmap[x, y] == 0:
                    y = np.where(self.flatmap[x] != 0)[0][-1]
            if self.face == "D":
                x = (x + 1) % self.height
                if self.flatmap[x, y] == 0:
                    x = np.where(self.flatmap[:, y] != 0)[0][0]
            if self.face == "U":
                x = (x - 1 + self.height) % self.height
                if self.flatmap[x, y] == 0:
                    x = np.where(self.flatmap[:, y] != 0)[0][-1]

            if self.flatmap[x, y] == 9:
                break

            self.position = (x, y)

    def Fold_turn(self, direction):
        index = self.faces.index(self.face)
        if direction == "R":
            self.face = self.faces[(index + 1) % 4]
        if direction == "L":
            self.face = self.faces[(index - 1) % 4]

        current_square = self.minifold[self.position[0] // self.squaresize][self.position[1] // self.squaresize]
        turn_info = self.turndict[current_square][self.face]
        self.position = (self.position[0] + turn_info[1], self.position[1] + turn_info[1])
        self.face = self.faces[(index + turn_info[0]) % 4]


facepoints = {"R": 0, "D": 1, "L": 2, "U": 3}
with open('2022-22Monkey_Map.txt') as f:
    lines = f.read().splitlines()

route = lines[-1]
landscape = Grid(lines[:-2])
coord, face = landscape.Route(route)

print("PART 1: answer to part 1 =", 1000 * (coord[0] + 1) + 4 * (coord[1] + 1) + facepoints[face],
      "\n\t cause row is", coord[0] + 1, ",and column is", coord[1] + 1, " and the face is", face)

cubelandscape = Cube(lines[:-2])
# coord, face = cubelandscape.Route(route)

print("PART 2: answer to part 2 =", 1000 * (coord[0] + 1) + 4 * (coord[1] + 1) + facepoints[face],
      "\n\t cause row is", coord[0] + 1, ",and column is", coord[1] + 1, " and the face is", face)
