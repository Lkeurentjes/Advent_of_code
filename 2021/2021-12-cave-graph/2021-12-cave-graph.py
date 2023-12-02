class Node:
    def __init__(self, name):
        self.name = name
        self.start = name == "start"
        self.end = name == "end"
        self.big = name.isupper() and not self.start and not self.end
        self.connected = set()
    def connect(self, other):
        self.connected.add(other)


class Graph:
    def __init__(self, lines):
        self.nodedict = {}
        for l in lines:
            l = l.split("-")
            if l[0] not in self.nodedict:
                self.nodedict[l[0]] = Node(l[0])
            if l[1] not in self.nodedict:
                self.nodedict[l[1]] = Node(l[1])
            self.nodedict[l[0]].connect(self.nodedict[l[1]])
            self.nodedict[l[1]].connect(self.nodedict[l[0]])

    def find_correct_paths(self, path, next):
        newpath = path + [next]
        nextN = self.nodedict[next]
        if nextN.end:
            # print(newpath)
            return 1
        elif not nextN.big and nextN.name in path:
            return 0
        else:
            return sum(self.find_correct_paths(newpath, cN.name) for cN in nextN.connected)


    def find_correct_paths_twice(self, path, next, twice):
        newpath = path + [next]
        nextN = self.nodedict[next]
        visitnot = False
        if not nextN.big:
            count = path.count(nextN.name)
            visitnot = (twice and count > 0) or (newpath.count("start") == 2)
            twice = (count == 1) or twice

        if nextN.end:
            # print(newpath)
            return 1
        elif visitnot:
            return 0
        else:
            return sum(self.find_correct_paths_twice(newpath, cN.name,twice) for cN in nextN.connected)



with open('2021-12-cave-graph.txt') as f:
    lines = f.read().splitlines()

caves = Graph(lines)
print("Part 1, number of paths is", caves.find_correct_paths([], "start"))
print("Part 2, number of paths is", caves.find_correct_paths_twice([], "start", False))
