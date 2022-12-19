import numpy as np
from collections import deque
import copy
import time

def getobjects(state):
    # change state
    state[0] += state[4]
    state[1] += state[5]
    state[2] += state[6]
    state[3] += state[7]
    state[8] -= 1
    return state

def todo(state, oreR, clayR,obsidianR,geodeR):
    best = 0
    seen = set()

    queue = deque([state])
    # queue = [state]
    while len(queue):
        # print(best)
        currentstate = queue.popleft()

        best = max(currentstate[3], best)
        if currentstate[8] <= 0:
            continue

        #add max for robots
        max_ores = max([oreR,clayR,obsidianR[0],geodeR[0]])

        # Core = max([Co, Cc, Co1, Cg1])
        # if r1 >= Core:
        #     r1 = Core
        # if r2 >= Co2:
        #     r2 = Co2
        # if r3 >= Cg2:
        #     r3 = Cg2
        # if o >= t * Core - r1 * (t - 1):
        #     o = t * Core - r1 * (t - 1)
        # if c >= t * Co2 - r2 * (t - 1):
        #     c = t * Co2 - r2 * (t - 1)
        # if ob >= t * Cg2 - r3 * (t - 1):
        #     ob = t * Cg2 - r3 * (t - 1)
        #
        # state = (o, c, ob, g, r1, r2, r3, r4, t)

        if tuple(currentstate) in seen:
            continue

        maxgeodes = 0
        maxgeodes += currentstate[3] + currentstate[7]*currentstate[8]
        if currentstate[6] > 0:
            roundstobuy = max(geodeR[0]//currentstate[4], geodeR[1]//currentstate[6])
            for i in range(currentstate[8]//roundstobuy):
                maxgeodes += roundstobuy*i
        if maxgeodes < best:
            continue


        seen.add(tuple(currentstate))
        #check buy options
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

            if currentstate[0] >= oreR and currentstate[4]<max_ores:

                nextstate = copy.deepcopy(currentstate)
                #pay money
                nextstate[0] -= oreR
                # get objects and - 1 minutes
                nextstate = getobjects(nextstate)
                #get robot
                nextstate[4] += 1
                #add state to queue
                # print("buy R1", nextstate)
                queue.append(nextstate)

            if currentstate[0] >= clayR and currentstate[5]< obsidianR[1]:

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

            if currentstate[0] >= obsidianR[0] and currentstate[1] >= obsidianR[1] and currentstate[6]<geodeR[1]:

                nextstate = copy.deepcopy(currentstate)
                # pay money
                nextstate[0] -= obsidianR[0]
                nextstate[1] -= obsidianR[1]
                # get objects and - 1 minutes
                nextstate= getobjects(nextstate)
                # get robot
                nextstate[6] += 1
                # add state to queue
                # print("buy R3", nextstate)
                queue.append(nextstate)



    return best

def maxgeodes(blueprint,minutes):
    #the costs
    oreR = blueprint[0]
    clayR = blueprint[1]
    obsidianR = (blueprint[2],blueprint[3])
    geodeR = (blueprint[4], blueprint[5])

    #state = (ore,clay,obsidian,geode,oreRobot,ClayRobot,ObsidianRobot,GeodeRobot,minutes)
    state = [0,0,0,0,1,0,0,0,minutes]
    return todo(state, oreR, clayR,obsidianR,geodeR)


MINUTES = 24
with open("202219geodes.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    blueprintdict = {}
    for i in range(len(lines)):
        line = lines[i].split(" ")
        # print(line)
        # print(i, int(line[6]),int(line[12]),int(line[18]),int(line[21]),int(line[27]),int(line[30]))
        blueprintdict[i+1] = [int(line[6]),int(line[12]),int(line[18]),int(line[21]),int(line[27]),int(line[30])]

    print(blueprintdict)
    for i,blueprint in blueprintdict.items():
        start = time.time()
        blueprintdict[i] = maxgeodes(blueprint, MINUTES)
        print("worked ", (time.time()-start), "seconds on blueprint", i , "with maxgeodes is:", blueprintdict[i])
    print(blueprintdict)

    totalscore = 0
    for index, score in blueprintdict.items():
        totalscore += index*score
    print("PART 1 ANSWER IS: ", totalscore)