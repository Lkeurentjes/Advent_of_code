from math import gcd
class Graph:
    def __init__(self, lines):
        self.nodedict = {}
        self.ghostcurrent = []
        self.ghostfinish = False
        for l in lines:
            l = l.replace("=", " ").replace("(", " ").replace(")", " ").replace(",", " ").split()
            self.nodedict[l[0]] = (l[1],l[2])
            if l[0][-1] == "A":
                self.ghostcurrent.append(l[0])
        self.current = "AAA"
        self.finish = "ZZZ"

    def walk(self, route):
        steps = 0
        while self.current != self.finish:
            LR = route[(steps) % len(route)]
            if LR == "R":
                self.current = self.nodedict[self.current][1]
            else:
                self.current = self.nodedict[self.current][0]
            steps += 1
        return steps

    def ghost_route(self, route):
        T = {}
        steps = 0
        while True:
            LR = route[(steps) % len(route)]
            for i, node in enumerate(self.ghostcurrent):
                if LR == "R":
                    self.ghostcurrent[i] = self.nodedict[node][1]
                else:
                    self.ghostcurrent[i] = self.nodedict[node][0]
                if self.ghostcurrent[i].endswith('Z'):
                    # to get all steps to a z node
                    # update when coming across a new z node
                    T[i] = steps+1
                    if len(T) == len(self.ghostcurrent):
                        return self.lcm(T.values())
            self.ghostfinish = all(node[-1] == "Z" for node in self.ghostcurrent)
            steps += 1

    def lcm(self, xs):
        ans = 1
        for x in xs:
            ans = (x*ans)//gcd(x,ans)
        return ans

with open('2023-08-Dessert-graph.txt') as f:
    lines = f.read().splitlines()

route = lines[0]
Dessert = Graph(lines[2::])
print("Part 1, the number of steps is", Dessert.walk(route))
print("Part 2, the number of steps in the ghost route", Dessert.ghost_route(route))

