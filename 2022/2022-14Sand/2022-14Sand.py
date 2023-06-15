import numpy as np

class Grid:
    def __init__(self, lines):
        print(lines)
        self.sandpaths = []
        self.maxx = 0
        self.minx = 1000
        self.maxy = 0
        self.miny = 1000
        for line in lines:
            sandpath = []
            line = line.split(" -> ")
            for l in line:
                l = list(map(int,l.split(",")))
                if l[0]<self.minx:
                    self.minx = l[0]
                if l[0]>self.maxx:
                    self.maxx = l[0]
                if l[1]>self.maxy:
                    self.maxy = l[1]
                sandpath.append(l)
            self.sandpaths.append(sandpath)
        # print(self.sandpaths)
        # print(self.minx, self.maxx, self.maxy)
        #part 2 stuff
        self.widder = (self.maxy+2)*2
        self.maxy+=2

        self.width = self.maxx-self.minx+1+self.widder
        self.grid = np.zeros((self.maxy+1, self.width))

        self.minx -= (self.widder // 2)
        # self.grid[0][500-self.minx] = 77
        self.makesandpaths()




    def makesandpaths(self):
        for path in self.sandpaths:

            for i in range(len(path)-1):

                stepH = path[i+1][0] -path[i][0]
                if stepH < 0:

                    for j in range(0,stepH-1,-1):
                        self.grid[path[i][1]][path[i][0] - self.minx +j] = 88

                if stepH > 0:

                    for j in range(0,stepH+1):
                        self.grid[path[i][1] ][path[i][0] - self.minx +j] = 88


                stepV =path[i + 1][1] - path[i][1]
                if stepV < 0:

                    for j in range(0,stepV-1,-1):
                        self.grid[path[i][1] +j][path[i][0] - self.minx] = 88
                if stepV > 0:

                    for j in range(0,stepV+1):
                        self.grid[path[i][1] +j][path[i][0] - self.minx] = 88

        for i in range(self.width):
            self.grid[self.maxy][i] = 88

        np.savetxt("1214matrix1.txt", self.grid, fmt='% 4d')


    def sandflow(self):
        counter = 0
        stop=True
        while stop:
            coord = self.horizontalfinder(500-self.minx,0)
            # print(coord)
            if coord == (10000,10000):
                stop = False
            if coord == (500 - self.minx,0):
                counter += 1
                self.grid[coord[1]][coord[0]] = 1
                stop = False
            else:
                counter += 1
                self.grid[coord[1]][coord[0]] = 1
                np.savetxt("1214matrix.txt", self.grid, fmt='% 4d')
                # print(self.grid)


        # self.grid.tofile("1214matrix.txt")
        np.savetxt("1214matrix.txt",self.grid, fmt='% 4d')
        return counter

    def diagonalfinder(self,X,Y):
        if self.grid[Y][X-1] == 0:
            return self.horizontalfinder(X-1, Y)
        if self.grid[Y][X+1] == 0:
            return self.horizontalfinder(X+1, Y)
        else:
            return (X,Y-1)

    def horizontalfinder(self,X,Y):
        if X<0 or Y<0 or X>self.width or Y>self.maxy:
            return (10000, 10000)
        print(X,Y, self.maxy)
        for i in range(Y,self.maxy+1,1):
            print(X,i)
            if self.grid[i][X] != 0:
                return self.diagonalfinder(X,i)
        print("\n\n\n\n\nI SHOULD NOT BE HEEEEERE\n\n\n\n\n")
        return (10000,10000)

with open('2022-14Sand.txt') as f:
    lines = f.read().splitlines()
    landscape = Grid(lines)
    print(landscape.sandflow())

