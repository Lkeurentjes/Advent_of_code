import math
from itertools import zip_longest

def Makesum(Numbers):
    Numberlist = []
    sum = []
    for column in zip_longest(*Numbers, fillvalue=" "):
        combined = "".join(column)
        if not combined.replace(" ", "").isdigit():
            Numberlist.append(sum)
            sum = []
        else:
            sum.append(int(combined))
    Numberlist.append(sum)
    
    return Numberlist



def RtLMath (lines):
    Numbers = Makesum(lines[:-1])
    Operators = lines[-1].split()

    result = 0
    for i, operator in enumerate(Operators):
        if operator == "+":
            result += sum(Numbers[i])
        if operator == "*":
            result += math.prod(Numbers[i])
    return result


def MathHomework(lines):
    Numbers = lines[:-1]
    Operators = lines[-1]
    result = 0
    for i, operator in enumerate(Operators):
        nums = [int(num[i]) for num in Numbers]
        if operator == "+":
            result += sum(nums)
        if operator == "*":
            result += math.prod(nums)
    return result


with open('2025-06-TrashCompactor.txt') as f:
    lines = [line.split() for line in f.read().splitlines()]
    print("Part 1",MathHomework(lines))

with open('2025-06-TrashCompactor.txt') as f:
    lines = f.read().splitlines()
    print("Part 2",RtLMath(lines))