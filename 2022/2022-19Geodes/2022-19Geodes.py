import numpy as np
from collections import deque
import copy
import time
from itertools import islice


def getobjects(state):
    # change state
    state[0] += state[4]
    state[1] += state[5]
    state[2] += state[6]
    state[3] += state[7]
    state[8] -= 1
    return state


def todo(state, oreR, clayR, obsidianR, geodeR):
    best = 0
    seen = set()

    queue = deque([state])
    # queue = [state]
    while len(queue):
        # print(best)
        currentstate = queue.popleft()
        best = max(currentstate[3], best)

        if currentstate[8] <= 0:
            finishstate = getobjects(currentstate)
            best = max(finishstate[3], best)
            continue

        # add max for robots
        max_ores = max([oreR, clayR, obsidianR[0], geodeR[0]])

        # change to lower values with same effect to speed up the search
        currentstate[0] = min(currentstate[0], (currentstate[8] * max_ores - currentstate[4] * (currentstate[8] - 1)))
        currentstate[1] = min(currentstate[1], (currentstate[8] * obsidianR[1] - currentstate[5] * (currentstate[8] - 1)))
        currentstate[2] = min(currentstate[2], (currentstate[8] * geodeR[1] - currentstate[6] * (currentstate[8] - 1)))

        if tuple(currentstate) in seen:
            continue

        maxgeodes = 0
        maxgeodes += currentstate[3] + currentstate[7] * currentstate[8]
        if currentstate[6] > 0:
            roundstobuy = max(geodeR[0] // currentstate[4], geodeR[1] // currentstate[6])
            for i in range(currentstate[8] // roundstobuy):
                maxgeodes += roundstobuy * i
        if maxgeodes < best:
            continue

        seen.add(tuple(currentstate))
        seen.add(tuple(currentstate))
        # check buy options
        # state = (ore,clay,obsidian,geode,oreRobot,ClayRobot,ObsidianRobot,GeodeRobot,minutes)
        if currentstate[0] >= geodeR[0] and currentstate[2] >= geodeR[1]:

            nextstate = copy.deepcopy(currentstate)
            # pay money
            nextstate[0] -= geodeR[0]
            nextstate[2] -= geodeR[1]
            # get objects and - 1 minutes
            nextstate = getobjects(nextstate)
            # get robot
            nextstate[7] += 1
            # add state to queue
            # print("buy R4",nextstate)
            queue.append(nextstate)
        else:
            nextstate = copy.deepcopy(currentstate)
            # get objects and - 1 minutes
            nextstate = getobjects(nextstate)
            # add state to queue
            queue.append(nextstate)

            if currentstate[0] >= oreR and currentstate[4] < max_ores:
                nextstate = copy.deepcopy(currentstate)
                # pay money
                nextstate[0] -= oreR
                # get objects and - 1 minutes
                nextstate = getobjects(nextstate)
                # get robot
                nextstate[4] += 1
                # add state to queue
                # print("buy R1", nextstate)
                queue.append(nextstate)

            if currentstate[0] >= clayR and currentstate[5] < obsidianR[1]:
                nextstate = copy.deepcopy(currentstate)
                # pay money
                nextstate[0] -= clayR
                # get objects and - 1 minutes
                nextstate = getobjects(nextstate)
                # get robot
                nextstate[5] += 1
                # add state to queue
                # print("buy R2", nextstate)
                queue.append(nextstate)

            if currentstate[0] >= obsidianR[0] and currentstate[1] >= obsidianR[1] and currentstate[6] < geodeR[1]:
                nextstate = copy.deepcopy(currentstate)
                # pay money
                nextstate[0] -= obsidianR[0]
                nextstate[1] -= obsidianR[1]
                # get objects and - 1 minutes
                nextstate = getobjects(nextstate)
                # get robot
                nextstate[6] += 1
                # add state to queue
                # print("buy R3", nextstate)
                queue.append(nextstate)

    return best


def maxgeodes(blueprint, minutes):
    # the costs
    oreR = blueprint[0]
    clayR = blueprint[1]
    obsidianR = (blueprint[2], blueprint[3])
    geodeR = (blueprint[4], blueprint[5])

    # state = (ore,clay,obsidian,geode,oreRobot,ClayRobot,ObsidianRobot,GeodeRobot,minutes)
    state = [0, 0, 0, 0, 1, 0, 0, 0, minutes]
    return todo(state, oreR, clayR, obsidianR, geodeR)


with open('2022-19Geodes.txt') as f:
    lines = f.read().splitlines()

    blueprintdict = {}
    for i in range(len(lines)):
        line = lines[i].split(" ")
        # print(line)
        # print(i, int(line[6]),int(line[12]),int(line[18]),int(line[21]),int(line[27]),int(line[30]))
        blueprintdict[i + 1] = [int(line[6]), int(line[12]), int(line[18]), int(line[21]), int(line[27]), int(line[30])]

    blueprintdict2 = copy.deepcopy(blueprintdict)

    # part 1
    MINUTES = 24
    for i, blueprint in blueprintdict.items():
        start = time.time()
        blueprintdict[i] = maxgeodes(blueprint, MINUTES - 1)
        print("worked ", (time.time() - start), "seconds on blueprint", i, "with maxgeodes is:", blueprintdict[i])
    # print(blueprintdict)

    totalscore = 0
    for index, score in blueprintdict.items():
        totalscore += index * score
    print("PART 1 ANSWER IS: ", totalscore)

    # part 2
    MINUTES = 32
    for i, blueprint in islice(blueprintdict2.items(), 3):
        start = time.time()
        blueprintdict2[i] = maxgeodes(blueprint, MINUTES - 1)
        print("worked", (time.time() - start), "seconds on blueprint", i, "with maxgeodes is:", blueprintdict2[i])

    totalscore = 1
    for index, score in islice(blueprintdict2.items(), 3):
        totalscore *= score
    print("PART 2 ANSWER IS: ", totalscore)
