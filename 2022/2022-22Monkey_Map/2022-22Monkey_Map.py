import numpy as np


class Grid:
    def __init__(self, lines):
        self.faces = ["U", "R", "D", "L"]
        self.height = len(lines)
        self.width = max(len(l) for l in lines)
        self.map = np.zeros((self.height, self.width))
        self.makemap(lines)
        self.position = (0, np.where(self.map[0] == 1)[0][0])
        self.face = "R"

        # #part2
        # self.cubemap = np.zeros((self.height, self.width))
        # self.minifold = None

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

        # flat part
        self.heightflat = len(lines)
        self.widthflat = max(len(l) for l in lines)
        self.flatmap = np.zeros((self.heightflat, self.widthflat))
        self.makemap(lines)

        # to cube
        self.squaresize = abs(self.heightflat - self.widthflat)
        self.minifold = self.make_mini_fold()
        self.connection = {}
        self.make_conections()

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
        biggest = max(heigth, width)
        mini = np.zeros((biggest, biggest))
        index = 1
        for i in range(heigth):
            for j in range(width):
                if self.flatmap[i * self.squaresize][j * self.squaresize] != 0:
                    mini[i][j] = index
                    index += 1
        return mini

    def make_conections(self):
        heigth = self.heightflat // self.squaresize
        width = self.widthflat // self.squaresize
        maxx = max(heigth, width)
        neigbourdict = {"D": (1, 0), "R": (0, 1), "U": (-1, 0), "L": (0, -1)}
        mirrordict = {"D": "U", "R": "L", "U": "D", "L": "R"}

        turndict = {1:{},2:{},3:{},4:{},5:{},6:{}}

        for i in range(heigth):
            for j in range(width):
                if self.minifold[i][j] != 0:
                    conturndict = {}
                    # print(i, j)
                    for key, value in neigbourdict.items():
                        x, y = value

                        X = (i + x + maxx) % maxx
                        Y = (j + y + maxx) % maxx
                        # print(x,y,X,Y)
                        if self.minifold[X][Y] != 0:
                            conturndict[key] = (self.minifold[X][Y], 0)
                            turndict[int(self.minifold[i][j])][key] = (self.minifold[X][Y], 0)
                            turndict[int(self.minifold[X][Y])][mirrordict[key]] = (self.minifold[i][j], 0)
                            continue
                        # else:
                        #     if key == "U":
                        #         for r in range(1, 4):
                        #             if 0 <= Y - r < maxx:
                        #                 newY = Y- r
                        #                 if self.minifold[X][newY] != 0:
                        #                     conturndict[key] = (self.minifold[X][newY], -r * x)
                        #                     turndict[int(self.minifold[i][j])][key] = (self.minifold[X][newY], -r * x)
                        #                     if r == 2:
                        #                         turndict[int(self.minifold[X][newY])][key] = (self.minifold[i][j], r*x)
                        #                     break
                        #     if key == "R":
                        #         for r in range(1, 4):
                        #             if 0 <= X - r < maxx:
                        #                 newX = (X - r)
                        #                 if self.minifold[newX][Y] != 0:
                        #                     conturndict[key] = (self.minifold[newX][Y], -r * y)
                        #                     turndict[int(self.minifold[i][j])][key] = (self.minifold[newX][Y], -r*y)
                        #                     if r == 2:
                        #                         turndict[int(self.minifold[newX][Y])][mirrordict[key]] = (self.minifold[i][j], r*y)
                        #                     break
                        #     if key == "D":
                        #         for r in range(1, 4):
                        #             if 0 <= Y + r < maxx:
                        #                 newY = (Y + r )
                        #                 if self.minifold[X][newY] != 0:
                        #                     conturndict[key] = (self.minifold[X][newY], r * x)
                        #                     turndict[int(self.minifold[i][j])][key] = (self.minifold[X][newY], r * x)
                        #                     if r == 2:
                        #                         turndict[int(self.minifold[X][newY])][key] = (self.minifold[i][j], -r*x)
                        #                     break
                        #     if key == "L":
                        #         for r in range(1, 4):
                        #             if 0 <= X + r < maxx:
                        #                 newX = (X + r )
                        #                 if self.minifold[newX][Y] != 0:
                        #                     conturndict[key] = (self.minifold[newX][Y], r * y)
                        #                     turndict[int(self.minifold[i][j])][key] = (self.minifold[newX][Y], r*y)
                        #                     if r == 2:
                        #                         turndict[int(self.minifold[newX][Y])][mirrordict[key]] = (self.minifold[i][j], -r*y)
                        #                     break

                    # print(self.minifold[i][j], conturndict)
        print(turndict)

# def Route(self, route):
#     routelist = route.replace("R", " R ").replace("L", " L ").split()
#     for r in routelist:
#         if r.isdigit():
#             self.Walk(int(r))
#         else:
#             self.Turn(r)
#     return self.position, self.face
# def Walk(self, steps):
#     for s in range(steps):
#         x,y = self.position
#         if self.face == "R":
#             y = (y+1)
#             if y == self.width:
#                 a=1
#             elif self.map[x, y] == 0:
#                 a=2
#         if self.face == "L":
#             y = (y-1 + self.width) % self.width
#             if self.map[x, y] == 0:
#                 y = np.where(self.map[x] != 0)[0][-1]
#         if self.face == "D":
#             x = (x+1) % self.height
#             if self.map[x, y] == 0:
#                 x = np.where(self.map[:, y] != 0)[0][0]
#         if self.face == "U":
#             x = (x-1 + self.height) % self.height
#             if self.map[x, y] == 0:
#                 x = np.where(self.map[:, y] != 0)[0][-1]
#
#         if self.map[x, y] == 9:
#             break
#
#         self.position = (x, y)
#
# def Turn(self, direction):
#     index = self.faces.index(self.face)
#     if direction == "R":
#         self.face = self.faces[(index + 1) % 4]
#     if direction == "L":
#         self.face = self.faces[(index - 1) % 4]
#
# def Fold_turn(self, direction):
#     index = self.faces.index(self.face)
#     if direction == "R":
#         self.face = self.faces[(index + 1) % 4]
#     if direction == "L":
#         self.face = self.faces[(index - 1) % 4]


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
