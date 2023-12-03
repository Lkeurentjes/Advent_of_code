import numpy as np


class Grid:
    def __init__(self, lines):
        self.faces = ["N", "S", "W", "E"]
        self.consider = {"E": [(-1, 1), (0, 1), (1, 1)], "W": [(-1, -1), (0, -1), (1, -1)],
                         "N": [(-1, 1), (-1, 0), (-1, -1)], "S": [(1, 1), (1, 0), (1, -1)]}
        self.height = len(lines)
        self.width = max(len(l) for l in lines)
        self.map = np.zeros((self.height, self.width))
        self.makemap(lines)
        self.adjacent = {(-1, 1), (0, 1), (1, 1), (-1, 0),
                         (1, 0), (-1, -1), (0, -1), (1, -1)}
        self.elflocations = []

    def printgrid(self):
        for row in self.map:
            print("".join("#" if cell > 0 else "." for cell in row))

    def makemap(self, lines):
        for i, line in enumerate(lines):
            for j, l in enumerate(line):
                if l == "#":
                    self.map[i][j] = 1

    def walk(self, rounds):
        self.map = np.pad(self.map, rounds)
        for r in range(rounds):
            set_steps = set()
            step_elf_dict = {}
            elf_prop_dict = {}
            elfs = list(zip(np.where(self.map == 1)[0], np.where(self.map == 1)[1]))
            for xe, ye in elfs:
                stay = True
                for xa, ya in self.adjacent:
                    if self.map[xe + xa][ye + ya] != 0:
                        stay = False
                        break
                if not stay:
                    for dir in self.faces:
                        free = True
                        add = True
                        for cx, cy in self.consider[dir]:
                            if self.map[xe + cx][ye + cy] != 0:
                                free = False
                                break
                        if free:
                            xn = xe + self.consider[dir][1][0]
                            yn = ye + self.consider[dir][1][1]
                            if (xn, yn) in set_steps:
                                if step_elf_dict[(xn, yn)] in elf_prop_dict:
                                    elf_prop_dict.pop(step_elf_dict[(xn, yn)])
                            else:
                                elf_prop_dict[(xe, ye)] = (xn, yn)

                            step_elf_dict[(xn, yn)] = (xe, ye)
                            set_steps.add((xn, yn))
                            break

            for now, go in elf_prop_dict.items():
                self.map[now] = 0
                self.map[go] = 1


            self.faces = self.faces[1:] + [self.faces[0]]
            # print("After Round ", r +1)
            # self.printgrid()

        mask = self.map == 0
        rows = np.flatnonzero((~mask).sum(axis=1))
        cols = np.flatnonzero((~mask).sum(axis=0))
        self.map = self.map[rows.min():rows.max()+1, cols.min():cols.max()+1]
        self.printgrid()
        return np.count_nonzero(self.map == 0)

    def stop(self):
        round = 1
        while (True):
            self.map = np.pad(self.map, 1)
            set_steps = set()
            step_elf_dict = {}
            elf_prop_dict = {}
            elfs = list(zip(np.where(self.map == 1)[0], np.where(self.map == 1)[1]))
            for xe, ye in elfs:
                stay = True
                for xa, ya in self.adjacent:
                    if self.map[xe + xa][ye + ya] != 0:
                        stay = False
                        break
                if not stay:
                    for dir in self.faces:
                        free = True
                        add = True
                        for cx, cy in self.consider[dir]:
                            if self.map[xe + cx][ye + cy] != 0:
                                free = False
                                break
                        if free:
                            xn = xe + self.consider[dir][1][0]
                            yn = ye + self.consider[dir][1][1]
                            if (xn, yn) in set_steps:
                                if step_elf_dict[(xn, yn)] in elf_prop_dict:
                                    elf_prop_dict.pop(step_elf_dict[(xn, yn)])
                            else:
                                elf_prop_dict[(xe, ye)] = (xn, yn)

                            step_elf_dict[(xn, yn)] = (xe, ye)
                            set_steps.add((xn, yn))
                            break

            if len(elf_prop_dict) == 0:
                return round

            for now, go in elf_prop_dict.items():
                self.map[now] = 0
                self.map[go] = 1

            self.faces = self.faces[1:] + [self.faces[0]]
            round+=1






with open('2022-23-plant-Starfruit.txt') as f:
    lines = f.read().splitlines()

ground = Grid(lines)
print("Part 1, the empty ground after walk", ground.walk(10))
ground2 = Grid(lines)
print("Part 2, the empty ground after walk", ground2.stop())
