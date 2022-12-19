import copy

class Monkey:
    def __init__(self,number, items, operationsign, operationnumber, testnumber, iftrue, iffalse):
        self.modd = None
        self.number = number
        self.items = items
        self.operationnumber = operationnumber

        if operationnumber == "old":
            if operationsign == "*":
                self.operation = lambda x: x* x
            # elif operationsign == "+":
            #     self.operation = lambda x: x + x
            # elif operationsign == "-":
            #     self.operation = lambda x: x - x
            # elif operationsign == "/":
            #     self.operation = lambda x: x / x
        else:
            if operationsign == "*":
                self.operation = lambda x: x * int(self.operationnumber)
            elif operationsign == "+":
                self.operation = lambda x: x + int(self.operationnumber)
            elif operationsign == "-":
                self.operation = lambda x: x - int(self.operationnumber)
            # elif operationsign == "/":
            #     self.operation = lambda x: x / int(self.operationnumber)

        self.testnumber = testnumber
        self.test  = lambda num: num % self.testnumber == 0
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspect = 0


    def printall(self):
        print("this money has:", self.items)
        print("Operations is: ", self.operation)
        print("test is: ", self.test)
        print("true is: ", self.iftrue)
        print("false is: ", self.iffalse)

    def set_supermodulo(self, modd):
        self.modd = modd

    def actionPART1(self):
        actionlist = []
        for i in self.items:
            self.inspect+=1
            answer = self.operation(i)
            answer = answer // 3
            if self.test(answer):
                actionlist.append((self.iftrue, answer))
            else:
                actionlist.append((self.iffalse, answer))
        self.items = []
        return actionlist

    def actionPART2(self):
        actionlist = []
        for i in self.items:
            self.inspect+=1
            answer = self.operation(i)
            answer %= self.modd
            if self.test(answer):
                actionlist.append((self.iftrue, answer))
            else:
                actionlist.append((self.iffalse, answer))
        self.items = []
        return actionlist

    def catch(self, item):
        self.items.append(item)


monkeylist = []
with open('2022-11Monkeys.txt') as f:
    lines = f.read().splitlines()

numberofmonkeys = (len(lines) + 1) // 7
supermodulo = 1
for i in range(0, numberofmonkeys):
    items = list(map(int, lines[1 + (i * 7)].strip("  Starting items: ").split(", ")))
    operationline = lines[2 + (i * 7)].removeprefix("  Operation: new = old ").split(" ")
    testnumber = int(lines[3 + (i * 7)].strip("  Test: divisible by "))
    supermodulo *= testnumber
    iftrue = int(lines[4 + (i * 7)].strip("    If true: throw to monkey "))
    iffalse = int(lines[5 + (i * 7)].strip("    If false: throw to monkey "))
    m = Monkey(i,items,operationline[0], operationline[1],testnumber,iftrue,iffalse)
    monkeylist.append(m)

monkeylist2 = copy.deepcopy(monkeylist)

ROUNDS = 20
for i in range(ROUNDS):
    # print(i)
    for monkey in monkeylist:
        throws = monkey.actionPART1()
        # print(throws)
        for i,item in throws:
            monkeylist[i].catch(item)

inspectations =[]
for monkey in monkeylist:
    # print(monkey.items)
    # print(monkey.inspect)
    inspectations.append(monkey.inspect)

largest_integer = max(inspectations)
inspectations.remove(largest_integer)

second_largest_integer = max(inspectations)
print("Part 1: the level of monkey buisiness is",(largest_integer*second_largest_integer))


### PART 2
for monkey in monkeylist2:
    monkey.set_supermodulo(supermodulo)


ROUNDS = 10000
for i in range(ROUNDS):
    # print(i)
    for monkey in monkeylist2:
        throws = monkey.actionPART2()
        # print(throws)
        for i,item in throws:
            monkeylist2[i].catch(item)

inspectations =[]
for monkey in monkeylist2:
    # print(monkey.items)
    # print(monkey.inspect)
    inspectations.append(monkey.inspect)

largest_integer = max(inspectations)
inspectations.remove(largest_integer)

second_largest_integer = max(inspectations)
print("Part 2: the level of monkey buisiness is",(largest_integer*second_largest_integer))




