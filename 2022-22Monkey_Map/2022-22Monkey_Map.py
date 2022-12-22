import numpy as np

class Grid:
    def __init__(self, lines):
        self.faces = ["U", "R", "D", "L"]
        self.height = len(lines)
        self.width = 0
        for l in lines:
            self.width = max(self.width, len(l))
        self.map = np.zeros((self.height, self.width))
        self.makemap(lines)
        self.position = (0, np.where(self.map[0] == 1)[0][0])
        self.face = "R"

        #part2
        self.cubemap = np.zeros((self.height, self.width))

        print(self.map)
        print(self.position)

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
            if self.face == "R":
                x = self.position[0]
                y = self.position[1] + 1
                if y == self.width:
                    y = 0
                if self.map[(x, y)] == 1:
                    self.position = (x, y)
                if self.map[(x, y)] == 9:
                    break
                if self.map[(x, y)] == 0:
                    y = np.where(self.map[x] != 0)[0][0]
                    if self.map[(x,y)] == 9:
                        break
                    self.position = (x, y)

            if self.face == "L":
                x = self.position[0]
                y = self.position[1] - 1
                if y == -1:
                    y = self.width-1
                if self.map[(x, y)] == 1:
                    self.position = (x, y)
                if self.map[(x, y)] == 9:
                    break
                if self.map[(x, y)] == 0:
                    y = np.where(self.map[x] != 0)[0][-1]
                    if self.map[(x,y)] == 9:
                        break
                    self.position = (x, y)
                    # self.position = (x, np.where(self.map[x] == 1)[0][-1])

            if self.face == "D":
                x = self.position[0] + 1
                y = self.position[1]
                if x == self.height:
                    x = 0
                if self.map[(x, y)] == 1:
                    self.position = (x, y)
                if self.map[(x, y)] == 9:
                    break
                if self.map[(x, y)] == 0:
                    x = np.where(self.map[:, y] != 0)[0][0]
                    if self.map[(x, y)] == 9:
                        break
                    self.position = (x, y)



            if self.face == "U":
                x = self.position[0] - 1
                y = self.position[1]
                if x == -1:
                    x = self.height-1
                if self.map[(x, y)] == 1:
                    self.position = (x, y)
                if self.map[(x, y)] == 9:
                    break
                if self.map[(x, y)] == 0:
                    x = np.where(self.map[:, y] != 0)[0][-1]
                    if self.map[(x, y)] == 9:
                        break
                    self.position = (x, y)



    def Turn(self, direction):
        if direction == "R":
            index = self.faces.index(self.face)
            if index == 3:
                self.face = self.faces[0]
            else:
                self.face = self.faces[index + 1]
        if direction == "L":
            index = self.faces.index(self.face)
            self.face = self.faces[index - 1]

    def makecube(self,SQUARE):
        h_cube = self.height//SQUARE
        w_cube = self.width//SQUARE
        counter = 1
        # print(h_cube,w_cube)
        for h in range(h_cube):
            for w in range(w_cube):
                x = h * (self.height // h_cube)
                y = w * (self.width // w_cube)
                if self.map[(x,y)] == 0:
                    continue

                for i in range(x,x+4):
                    for j in range(y, y+4):
                        self.cubemap[(i,j)] = counter
                counter +=1


                # print(x,y)
        print(self.cubemap)

class Cube:
    def __init__(self, landscape,size):
        self.landscape = landscape
        self.size = size
        self.landscape.makecube(size)

        self.faceslist = []
        self.makefaces()

    def makefaces(self):
        for i in range(1,7):
            locationsi = list(zip(np.where(self.landscape.cubemap == i)[0],np.where(self.landscape.cubemap == i)[1]))
            locationsf = list(zip(sorted([*range(self.size)]*self.size),[*range(self.size)]*self.size ))
            grid = np.zeros((self.size,self.size))
            for j in range(len(locationsf)):
                grid[locationsf[j]] = self.landscape.map[locationsi[j]]
            face = Face(i, grid,locationsi[0])
            self.faceslist.append(face)

    def setorientation(self):
        pass



class Face:
    def __init__(self, id, face, start):
        self.id = id
        self.positionlu= start
        self.face = face

        self.leftNeigbour = None
        self.leftrotation = None

        self.rightNeigbour = None
        self.rightrotation = None

        self.upNeigbour = None
        self.uprotation = None

        self.downNeigbour = None
        self.downrotation = None


facepoints= {"R":0,"D":1,"L":2,"U":3}
with open('2022-22Monkey_Map.txt') as f:
    lines = f.read().splitlines()
route = lines[-1]
landscape = Grid(lines[:-2])
coord, face = landscape.Route(route)
print("PART 1: answer to part 1 =", 1000*(coord[0]+1)+ 4*(coord[1]+1) + facepoints[face],
      "\n\t cause row is",coord[0]+1 ,",and column is", coord[1]+1, " and the face is", face)

SQUARE = 4
cubelandscape = Cube(landscape,SQUARE)

