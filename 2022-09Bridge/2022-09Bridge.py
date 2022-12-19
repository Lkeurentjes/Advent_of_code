import copy

class Grid:
    def __init__(self, lines):

        self.steps = []
        positionx = 0
        positiony = 0
        Maxx = 0
        Maxy = 0
        Minx = 0
        Miny = 0
        for i in lines:
            what = i.split()
            if what[0] == "U":
                positionx -= int(what[1])
                if Minx > positionx: Minx = positionx
            if what[0] == "D":
                positionx += int(what[1])
                if Maxx < positionx: Maxx = positionx
            if what[0] == "L":
                positiony -= int(what[1])
                if Miny > positiony: Miny = positiony
            if what[0] == "R":
                positiony += int(what[1])
                if Maxy < positiony: Maxy = positiony
            self.steps.append((what[0], int(what[1])))
        self.height = -Minx + Maxx + 1
        self.width = -Miny + Maxy + 1
        self.start = (-Minx, -Miny)
        self.visited = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(".")
            self.visited.append(row)
        self.visited[self.start[0]][self.start[1]] = "#"
        self.visited9 = copy.deepcopy(self.visited)


        self.head = self.start
        self.tail = self.start

        self.head9 = self.start
        self.t1 = self.start
        self.t2 = self.start
        self.t3 = self.start
        self.t4 = self.start
        self.t5 = self.start
        self.t6 = self.start
        self.t7 = self.start
        self.t8 = self.start
        self.tail9 = self.start



    def printgrid(self):
        for i in self.visited:
            # pass
            print(i)

    def walk(self):
        for step in self.steps:
            # print(step)
            if step[0] == "U":
                for i in range(step[1]):
                    self.head = (self.head[0] - 1, self.head[1])
                    self.tail = self.movetail(self.head, self.tail)
                    self.visited[self.tail[0]][self.tail[1]] = "#"
                    # self.printgrid()
            if step[0] == "D":
                for i in range(step[1]):

                    self.head = (self.head[0] + 1, self.head[1])
                    self.tail = self.movetail(self.head, self.tail)
                    self.visited[self.tail[0]][self.tail[1]] = "#"
                    # self.printgrid()
            if step[0] == "L":
                for i in range(step[1]):
                    self.head = (self.head[0], self.head[1] - 1)
                    self.tail = self.movetail(self.head, self.tail)
                    self.visited[self.tail[0]][self.tail[1]] = "#"
                    # self.printgrid()
            if step[0] == "R":
                for i in range(step[1]):
                    self.head = (self.head[0], self.head[1] + 1)
                    self.tail = self.movetail(self.head, self.tail)
                    self.visited[self.tail[0]][self.tail[1]] = "#"
                    # self.printgrid()


    def walk9(self):
        for step in self.steps:
            # print(step)
            if step[0] == "U":
                for i in range(step[1]):
                    self.head9 = (self.head9[0] - 1, self.head9[1])
                    self.t1 = self.movetail(self.head9, self.t1)
                    self.t2 = self.movetail(self.t1, self.t2)
                    self.t3 = self.movetail(self.t2, self.t3)
                    self.t4 = self.movetail(self.t3, self.t4)
                    self.t5 = self.movetail(self.t4, self.t5)
                    self.t6 = self.movetail(self.t5, self.t6)
                    self.t7 = self.movetail(self.t6, self.t7)
                    self.t8 = self.movetail(self.t7, self.t8)
                    self.tail9 = self.movetail(self.t8, self.tail9)
                    self.visited9[self.tail9[0]][self.tail9[1]] = "#"
                    # self.printgrid()
            if step[0] == "D":
                for i in range(step[1]):
                    self.head9 = (self.head9[0] + 1, self.head9[1])
                    self.t1 = self.movetail(self.head9, self.t1)
                    self.t2 = self.movetail(self.t1, self.t2)
                    self.t3 = self.movetail(self.t2, self.t3)
                    self.t4 = self.movetail(self.t3, self.t4)
                    self.t5 = self.movetail(self.t4, self.t5)
                    self.t6 = self.movetail(self.t5, self.t6)
                    self.t7 = self.movetail(self.t6, self.t7)
                    self.t8 = self.movetail(self.t7, self.t8)
                    self.tail9 = self.movetail(self.t8, self.tail9)
                    self.visited9[self.tail9[0]][self.tail9[1]] = "#"
                    # self.printgrid()
            if step[0] == "L":
                for i in range(step[1]):
                    self.head9 = (self.head9[0], self.head9[1] - 1)
                    self.t1 = self.movetail(self.head9, self.t1)
                    self.t2 = self.movetail(self.t1, self.t2)
                    self.t3 = self.movetail(self.t2, self.t3)
                    self.t4 = self.movetail(self.t3, self.t4)
                    self.t5 = self.movetail(self.t4, self.t5)
                    self.t6 = self.movetail(self.t5, self.t6)
                    self.t7 = self.movetail(self.t6, self.t7)
                    self.t8 = self.movetail(self.t7, self.t8)
                    self.tail9 = self.movetail(self.t8, self.tail9)
                    self.visited9[self.tail9[0]][self.tail9[1]] = "#"
                    # self.printgrid()
            if step[0] == "R":
                for i in range(step[1]):
                    self.head9 = (self.head9[0], self.head9[1] + 1)
                    self.t1 = self.movetail(self.head9, self.t1)
                    self.t2 = self.movetail(self.t1, self.t2)
                    self.t3 = self.movetail(self.t2, self.t3)
                    self.t4 = self.movetail(self.t3, self.t4)
                    self.t5 = self.movetail(self.t4, self.t5)
                    self.t6 = self.movetail(self.t5, self.t6)
                    self.t7 = self.movetail(self.t6, self.t7)
                    self.t8 = self.movetail(self.t7, self.t8)
                    self.tail9 = self.movetail(self.t8, self.tail9)
                    self.visited9[self.tail9[0]][self.tail9[1]] = "#"
                    # self.printgrid()

    def movetail(self, head, tail):
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            if head[0] == tail[0]:
                if head[1] > tail[1]:
                    tail = (tail[0], tail[1] + 1)
                else:
                    tail = (tail[0], tail[1] - 1)
            elif head[1] == tail[1]:
                if head[0] > tail[0]:
                    tail = (tail[0] + 1, tail[1])
                else:
                    tail = (tail[0] - 1, tail[1])

            elif head[0] - tail[0] == -2:
                if head[1] > tail[1]:
                    tail = (tail[0] - 1, tail[1] + 1)
                else:
                    tail = (tail[0] - 1, tail[1] - 1)
            elif head[0] - tail[0] == 2:
                if head[1] > tail[1]:
                    tail = (tail[0] + 1, tail[1] + 1)
                else:
                    tail = (tail[0] + 1, tail[1] - 1)

            elif head[0] - tail[0] == -1:
                if head[1] > tail[1]:
                    tail = (tail[0] - 1, tail[1] + 1)
                else:
                    tail = (tail[0] - 1, tail[1] - 1)
            elif head[0] - tail[0] == 1:
                if head[1] > tail[1]:
                    tail = (tail[0] + 1, tail[1] + 1)
                else:
                    tail = (tail[0] + 1, tail[1] - 1)

        # print(abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1, "\t head", head,
        #       "tail", tail)
        return tail



with open('2022-09Bridge.txt') as f:
    lines = f.read().splitlines()
    # print(lines)
    bridge = Grid(lines)

    bridge.walk()
    counter = 0
    for row in bridge.visited:
        for place in row:
            if place == "#":
                counter += 1
    print("Part 1: ",counter, "positions are visited")

    bridge.walk9()
    counter2 = 0
    for row in bridge.visited9:
        for place in row:
            if place == "#":
                counter2 += 1
    print("Part 2: ",counter2, "positions are visited")
