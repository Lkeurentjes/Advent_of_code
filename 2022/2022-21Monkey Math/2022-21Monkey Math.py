from collections import deque

def recrursviveMath(answer,monkeydict):
    if isinstance(answer, int):
        return answer
    if answer[1] == "+":
        return recrursviveMath(monkeydict[answer[0]], monkeydict) + recrursviveMath(monkeydict[answer[2]], monkeydict)
    if answer[1] == "-":
        return recrursviveMath(monkeydict[answer[0]], monkeydict) - recrursviveMath(monkeydict[answer[2]], monkeydict)
    if answer[1] == "*":
        return recrursviveMath(monkeydict[answer[0]], monkeydict) * recrursviveMath(monkeydict[answer[2]], monkeydict)
    if answer[1] == "/":
        return recrursviveMath(monkeydict[answer[0]], monkeydict) // recrursviveMath(monkeydict[answer[2]], monkeydict)

def getbrokenpart(answer, monkeydict):
    if isinstance(answer, int):
        return 0, answer

    try:
        solution = recrursviveMath(monkeydict[answer[0]],monkeydict)
    except:
        return (answer[0], recrursviveMath(monkeydict[answer[2]],monkeydict))
    else:
        return (answer[2], solution)


TOKNOW = "root"
TODELETE = "humn"

with open('2022-21Monkey Math.txt') as f:
    lines = f.read().splitlines()

monkeydict = {}
for line in lines:
    line = line.replace(":","").split(" ")
    if len(line) == 4:
        monkeydict[line[0]] = [*line[1:]]
    else:
        monkeydict[line[0]] = int(line[1])

part1 = recrursviveMath(monkeydict[TOKNOW],monkeydict)
print("PART 1: Monkey Root will scream", part1)


del monkeydict[TODELETE]
broken, answer = getbrokenpart(monkeydict[TOKNOW], monkeydict)

while True:
    if broken == TODELETE:
        print("PART 2: We need to scream", answer)
        break
    mathtodo = monkeydict[broken]
    # print(broken, monkeydict[broken])
    broken, answer2 = getbrokenpart(monkeydict[broken], monkeydict)


    if mathtodo[1] == "+":
        answer -= answer2
    if mathtodo[1] == "-" and broken == mathtodo[0]:
        answer += answer2
    if mathtodo[1] == "-" and broken == mathtodo[2]:
        answer = -(answer-answer2)
    if mathtodo[1] == "*":
        answer //= answer2
    if mathtodo[1] == "/" and broken == mathtodo[0]:
        answer *= answer2
    if mathtodo[1] == "/" and broken == mathtodo[2]:
        answer //= answer2




# part2 = whattoscream(broken,answer, monkeydict)
# print(part2)


