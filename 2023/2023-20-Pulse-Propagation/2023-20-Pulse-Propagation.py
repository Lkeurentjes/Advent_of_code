import re
import math


class Node:
    def __init__(self, type, toward):
        self.to = toward
        self.type = type
        self.state = False
        self.last = {}

    def set_before(self, before):
        if self.type == "conjunction":
            for b in before:
                self.last[b] = 0
            # print(self.last)

    def send_signal(self, before, input):
        # print(self.type)
        if self.type == "broadcaster":
            return [(t, 0) for t in self.to]
        if self.type == "flip_flop":
            if input == 0:
                if self.state:
                    output = [(t, 0) for t in self.to]
                else:
                    output = [(t, 1) for t in self.to]
                self.state = not self.state
            else:
                output = []
            return output
        if self.type == "conjunction":
            self.last[before] = input
            # print(self.last)
            if all(p == 1 for p in self.last.values()):
                output = [(t, 0) for t in self.to]
            else:
                output = [(t, 1) for t in self.to]
            return output

    def original_state(self):
        if self.type == "broadcaster":
            return True
        if self.type == "flip_flop":
            return self.state is False
        if self.type == "conjunction":
            return all(p == 0 for p in self.last.values())

    def back_to_default(self):
        if self.type == "flip_flop":
            self.state = False
        if self.type == "conjunction":
            self.last = {key: 0 for key in self.last}

class Graph:
    def __init__(self, lines):
        self.graph = {}
        self.state = {}

        tofrom = {}
        for s, to in lines:
            name = "".join(re.findall("[a-zA-Z]+", s))
            if s[0] == "%":
                self.graph[name] = Node("flip_flop", to.split(", "))
            elif s[0] == "&":
                self.graph[name] = Node("conjunction", to.split(", "))
            else:
                self.graph[name] = Node("broadcaster", to.split(", "))
            tofrom[name] = to.split(", ")

        self.fromto = {}
        for k, v in tofrom.items():
            for x in v:
                self.fromto.setdefault(x, []).append(k)
        # print(self.fromto)

        for name, before in self.fromto.items():
            if name in self.graph.keys():
                self.graph[name].set_before(before)


    def find_cycle(self, max ,pt1, to, pt2):
        high, low, cycle = 0, 0, 0
        while (not all(value.original_state() for value in self.graph.values()) or cycle == 0):

            Queue = [("button", "broadcaster", 0)]
            low += 1
            while Queue:
                last, current, signal = Queue.pop(0)
                if pt2 and current == to and signal == 0:
                    return cycle+1
                if current not in self.graph.keys():
                    continue
                next = self.graph[current].send_signal(last, signal)
                for n, s in next:
                    Queue.append((current, n, s))
                    if s == 0:
                        low += 1
                    else:
                        high += 1
            cycle += 1
            if pt1 and cycle == max:
                break

        return high, low, cycle

    def click_button(self, times):
        h, l, c = self.find_cycle(1000, True, "", False)
        return (h * (times//c)) * (l * (times//c))

    def find_low(self, node):
        for value in self.graph.values():
            value.back_to_default()
        sender = self.fromto[node]
        dependson = self.fromto[sender[0]]
        subcycles = []
        for d in dependson:
            for value in self.graph.values():
                value.back_to_default()
            c = self.find_cycle(1, False, d, True)
            subcycles.append(c)
            print("\tsubcycle",d,c)
        return math.lcm(*subcycles)




with open('2023-20-Pulse-Propagation.txt') as f:
    lines = f.read().splitlines()
    lines = [line.split(" -> ") for line in lines]

Network = Graph(lines)
print("Part 1 after clicking the button the score =", Network.click_button(1000))
print("Part 2 rx is low after", Network.find_low("rx"))
