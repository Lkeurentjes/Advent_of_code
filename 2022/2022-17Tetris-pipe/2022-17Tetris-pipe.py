import numpy as np

class Grid:
    def __init__(self, jetstream):
        self.jetstream = jetstream
        self.jetindex = 0

        self.width = 7
        self.emptyheight = 3
        self.height = 4
        self.pipe = np.vstack(([8,8,8,8,8,8,8], np.zeros((self.emptyheight,self.width))))

        self.shape1 = [[1,1,1,1]]
        self.shape2 = [[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0]]
        self.shape3 = [[1, 1, 1],
                       [0, 0, 1],
                       [0, 0, 1]]
        self.shape4 = [[1],
                       [1],
                       [1],
                       [1]]
        self.shape5 = [[1, 1],
                       [1, 1]]

        self.checkleft = {1:[(0,0)],
                          2:[(1,0),(0,0),(2,0)],
                          3:[(0,0),(1,0),(2,0)],
                          4:[(0,0),(1,0),(2,0),(3,0)],
                          5:[(0,0),(1,0)]}
        self.checkright = {1:[(0,3)],
                           2:[(1,2),(0,0),(2,0)],
                           3:[(0,2),(1,0),(2,0)],
                           4:[(0,0),(1,0),(2,0),(3,0)],
                           5:[(0,1),(1,1)]}
        self.checkbottem = {1:[(0,0),(0,1),(0,2),(0,3)],
                            2:[(0,0),(1,0),(1,2)],
                            3:[(0,0),(0,1),(0,2)],
                            4:[(0,0)],
                            5:[(0,0),(0,1)]}

        self.shapeslist = [self.shape1,self.shape2,self.shape3,self.shape4,self.shape5]
        # for shape in self.shapeslist:
        #     print(shape)

    def printpipebackwards(self):
        for row in self.pipe[::-1]:
            print(row)

    def checkRIGHT(self,shape,shapenumber,addedpipe):
        for check in self.checkright[shapenumber]:
            if shape[check[0]][check[1]][1]==6:
                return False
            if addedpipe[shape[check[0]][check[1]][0]][shape[check[0]][check[1]][1]+1] != 0:
                return False
        return True

    def checkLEFT(self,shape,shapenumber,addedpipe):
        for check in self.checkleft[shapenumber]:
            if shape[check[0]][check[1]][1]==0:
                return False
            if addedpipe[shape[check[0]][check[1]][0]][shape[check[0]][check[1]][1]-1] != 0:
                return False
        return True

    def push(self,shape,shapenumber,addedpipe,stopped = False):
        if self.jetindex == len(self.jetstream)-1:
            self.jetindex = 0

        # print(self.jetstream[self.jetindex])
        if self.jetstream[self.jetindex] == ">":
            self.jetindex += 1
            if self.checkRIGHT(shape,shapenumber,addedpipe):
                for i in range(len(shape)):
                    for j in range(len(shape[i])):
                        shape[i][j][1] += 1
                if stopped:
                    if self.checkstop(shape, shapenumber, addedpipe):
                        self.stop(shape, shapenumber)
                    else:
                        self.down(shape, shapenumber, addedpipe)
                else:
                    self.down(shape, shapenumber, addedpipe)

            else:
                if stopped:
                    self.stop(shape, shapenumber)
                else:
                    self.down(shape, shapenumber, addedpipe)


        elif self.jetstream[self.jetindex] == "<":
            self.jetindex += 1
            if self.checkLEFT(shape,shapenumber,addedpipe):
                for i in range(len(shape)):
                    for j in range(len(shape[i])):
                        shape[i][j][1] -= 1

                if stopped:
                    if self.checkstop(shape, shapenumber, addedpipe):
                        self.stop(shape, shapenumber)
                    else:
                        self.down(shape, shapenumber, addedpipe)
                else:
                    self.down(shape, shapenumber, addedpipe)

            else:
                if stopped:
                    self.stop(shape, shapenumber)
                else:
                    self.down(shape, shapenumber, addedpipe)



    def checkstop(self,shape,shapenumber,addedpipe):
        # print(shape , "CHECKED")
        for check in self.checkbottem[shapenumber]:
            if addedpipe[shape[check[0]][check[1]][0] - 1][shape[check[0]][check[1]][1]] != 0:
                return True
        return False


    def down(self,shape,shapenumber,addedpipe):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                shape[i][j][0] -= 1

        if self.checkstop(shape, shapenumber, addedpipe):
            # self.stop(shape,shapenumber)
            self.push(shape, shapenumber, addedpipe,True)
        else:
            self.push(shape, shapenumber, addedpipe)





    def stop(self,shape,shapenumber):
        # print(shape)
        # print("\n")
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                coord = shape[i][j]
                self.pipe[coord[0]][coord[1]] = shapenumber

        emptyrows = 0
        for row in self.pipe[::-1]:
            sum = np.sum(row)
            if sum != 0:
                break
            else:
                emptyrows +=1

        for i in range(3-emptyrows):
            self.pipe = np.vstack((self.pipe, [0, 0, 0, 0, 0, 0, 0]))
        self.height += (3-emptyrows)
        # print(self.printpipebackwards())


    def makeshape_coord(self, shape):
        shapecoord = []
        for i in range(len(shape)):
            row = []
            for j in range(len(shape[i])):
                if shape[i][j] != 0:
                    coord = [self.height + i, 2 + j]
                    row.append(coord)
            shapecoord.append(row)
        # print(shapecoord)
        return shapecoord


    def fallingdown(self, rocks):
        rocksfive = rocks//5 +1
        rock = 0
        for i in range(rocksfive):

            if rock<rocks:
                rock+=1
                addedpipe = np.vstack((self.pipe,[0,0,0,0,0,0,0]))
                shape = self.makeshape_coord(self.shape1)
                self.push(shape,1,addedpipe)


            if rock<rocks:
                rock+=1
                addedpipe = np.vstack((self.pipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                shape = self.makeshape_coord(self.shape2)
                self.push(shape, 2, addedpipe)


            if rock<rocks:
                rock+=1
                addedpipe = np.vstack((self.pipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                shape = self.makeshape_coord(self.shape3)
                self.push(shape, 3, addedpipe)


            if rock<rocks:
                rock+=1
                addedpipe = np.vstack((self.pipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                shape = self.makeshape_coord(self.shape4)
                self.push(shape, 4, addedpipe)


            if rock<rocks:
                rock+=1
                addedpipe = np.vstack((self.pipe, [0, 0, 0, 0, 0, 0, 0]))
                addedpipe = np.vstack((addedpipe, [0, 0, 0, 0, 0, 0, 0]))
                shape = self.makeshape_coord(self.shape5)
                self.push(shape, 5, addedpipe)




with open('2022-17Tetris-pipe.txt') as f:
    line = f.read()
    Pipe = Grid(line)
    number_of_Rocks = 10
    # number_of_Rocks = 2022
    Pipe.fallingdown(number_of_Rocks)
    Pipe.printpipebackwards()
    print("height = ",Pipe.height-4)

