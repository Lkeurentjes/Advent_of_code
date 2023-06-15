import copy
import operator


class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.parent = None
        self.child = None

    def getvalues(self):
        return (self.index, self.value)

    def printNode(self):
        print("i am node", self.value, "and my index is now", self.index,
              "\n\t my parrent is", self.parent.getvalues(),
              "\n\t my childe is", self.child.getvalues())


def move(node,number):
    steps = node.value
    if abs(steps) >= number:
        if steps > 0:
            steps = steps% (number-1)
        if steps < 0:
            steps = - (abs(steps)%(number-1))

    for i in range(abs(steps)):
        if steps == 0:
            print("im here")
        if steps > 0:
            child = node.child


            child.child.parent = node
            node.parent.child = child

            child.parent, node.parent, child.child, node.child = node.parent, child, node, child.child
            # print(node.index, child.index)
            child.index, node.index = node.index, child.index

        if steps < 0:
            parent = node.parent


            parent.parent.child = node
            node.child.parent = parent

            node.parent, parent.parent, node.child, parent.child = parent.parent, node, parent, node.child
            # print(node.index, parent.index)
            parent.index, node.index = node.index, parent.index


with open('2022-20Encrypted.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    # print(lines)

TOKNOW = [1000, 2000, 3000]

numberofnodes = len(lines)
nodelist = []
nodelistp2 = []
answerpart1 = 0

for i in range(numberofnodes):
    n = Node(i, lines[i])
    n2 = Node(i, lines[i]*811589153)

    if nodelist != []:
        n.parent = nodelist[-1]
        n2.parent= nodelistp2[-1]

        nodelist[-1].child = n
        nodelistp2[-1].child = n2

    if i == len(lines) - 1:
        n.child = nodelist[0]
        nodelist[0].parent = n

        n2.child = nodelistp2[0]
        nodelistp2[0].parent = n2

    nodelist.append(n)
    nodelistp2.append(n2)



for n in nodelist:
    move(n,numberofnodes)

checklist = sorted(nodelist, key=operator.attrgetter('index'))
printer = []
for c in checklist:
    printer.append(c.value)

zero_index = printer.index(0)
for i in TOKNOW:
    # print(printer[(zero_index+ i) % len(lines)])
    answerpart1 +=printer[(zero_index+ i) % len(lines)]


print("PART 1: has", answerpart1, "as sum of the coordinates")

answerpart2 = 0
# for n in nodelistp2:
#     n.value *= 811589153

for i in range(10):
    for n in nodelistp2:
        move(n,numberofnodes)
    # print("Ran_one_Round")

checklist = sorted(nodelistp2, key=operator.attrgetter('index'))
printer = []
for c in checklist:
    printer.append(c.value)

zero_index = printer.index(0)
for i in TOKNOW:
    answerpart2 += printer[(zero_index + i) % len(lines)]

print("PART 2: has", answerpart2, "as sum of the coordinates")
