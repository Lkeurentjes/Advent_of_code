import re


class Graph:
    def __init__(self, lines):
        self.graph = {}
        self.state = {}
        self.all = set()
        for s, to in lines:
            flip = 1 if s[0] == "%" else 0
            name = " ".join(re.findall("[a-zA-Z]+", s))
            self.graph[name] = []
            self.state[name] = 0
            for t in to.split(", "):
                self.graph[name].append((flip, t))
                self.state[t] = 0
        print(self.state)
        print(self.graph)

    def find_cycle(self):
        high, low, cycle = 0, 0, 0
        while (not all(value == 0 for value in self.state.values()) or cycle == 0):
            Queue = [("broadcaster", 0)]
            while Queue:
                # print(Queue)
                current, state = Queue.pop(0)
                print(current, state)
                if current not in self.graph.keys():
                    continue
                self.state[current] = (self.state[current] + state) % 2
                if state == 0:
                    low += 1
                else:
                    high += 1
                for flip, to in self.graph[current]:
                    # self.state[to] = (self.state[to] + flip)%2
                    Queue.append((to, (state + flip) % 2))
                # self.state[current] = state
            print(self.state)
            cycle += 1
            # break
        return high, low, cycle

    def click_button(self, times):
        h, l, c = self.find_cycle()
        print(h, l, c)


with open('2023-20-Pulse-Propagation.txt') as f:
    lines = f.read().splitlines()
    lines = [line.split(" -> ") for line in lines]

Network = Graph(lines)
print("Part 1 after clicking the button the score =", Network.click_button(1000))
