import sys
import copy
import time
import itertools

sys.setrecursionlimit(15000)


class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed, nodes, edges, weight):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = nodes

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: {} for node in self.m_nodes}

        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])
        self.weight = weight

        self.distancegraph = copy.deepcopy(self.m_adj_list)
        self.add_distance()

        # self.print_adj_list()
        # print("\n")
        # self.print_dist_list()
        # print("\n")

        self.empty = []
        self.bestscore = 0
        self.bestpath = []

    # Add edge to the graph
    def add_edge(self, node1, node2, weight):
        self.m_adj_list[node1].update({node2: (2, weight)})

    # add distances
    def add_distance(self):
        for node in self.m_adj_list.keys():
            for to in self.m_adj_list.keys():
                if to not in self.m_adj_list[node].keys() and node != to:
                    value = self.Shortestpath(node, to)
                    # print(node,to,value)
                    self.distancegraph[node].update({to: (value, self.weight[to])})

    def Shortestpath(self, start, goal):
        explored = []
        queue = [[start]]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.m_adj_list[node]
                # print(neighbours)
                for neighbour in neighbours.keys():
                    # print(neighbour)
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        # print("jeeeej", *new_path)
                        return len(new_path)
                explored.append(node)

    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

    # Print the graph representation
    def print_dist_list(self):
        for key in self.distancegraph.keys():
            print("node", key, ": ", self.distancegraph[key])

    def find_most_points(self, start, path, score, steps):
        current_path = path + [start]
        # print(steps, score, path)

        if steps == 0:
            return score
            # if score > self.bestscore:
            #     self.bestscore = score

        best = score
        found = False
        for to,(dist,weight) in self.distancegraph[start].items():
            if to not in path and dist<steps:
                found = True
                newscore = score + (weight * (steps -dist))
                stepsleft = steps - dist
                result = self.find_most_points(to, current_path, newscore,stepsleft)
                if result > best:
                    best = result
        if found:
            return best

        return best

    def find_most_points_subgraph(self, start, path, score, steps, to_find):
        current_path = path + [start]
        # print(steps, score, path)

        if steps == 0:
            return score
            # if score > self.bestscore:
            #     self.bestscore = score

        best = score
        found = False
        for to,(dist,weight) in self.distancegraph[start].items():
            if to not in path and dist<steps:
                if to in to_find:
                    found = True
                    newscore = score + (weight * (steps -dist))
                    stepsleft = steps - dist
                    result = self.find_most_points_subgraph(to, current_path, newscore,stepsleft,to_find)
                    if result > best:
                        best = result
        if found:
            return best

        return best

    def find_most_points_together(self, startYou, startOllie, path, score, stepsYou, stepsOllie):
        # print(score,path,stepsYou,stepsOllie)
        best = score
        if stepsYou == 0 and stepsOllie == 0:
            return best

        if set(self.m_nodes) == set(path):
            return best


        elif stepsYou!= 0 and stepsOllie != 0 and stepsYou>=stepsOllie:
            current_path = path + [startYou] + [startOllie]
            foundY,foundO = False, False
            for toy,(disty,weighty) in self.distancegraph[startYou].items():
                if toy not in current_path and disty<stepsYou:
                    foundY = True
                    stepsleftY = stepsYou - disty
                    testpath = current_path+ [toy]
                    for toO, (distO, weightO) in self.distancegraph[startOllie].items():
                        if toO not in testpath and distO < stepsOllie:
                            foundO = True
                            newscore = score + (weightO * (stepsOllie - distO)) + (weighty * (stepsYou -disty))
                            stepsleftO = stepsOllie - distO
                            result = self.find_most_points_together(toy, toO, current_path, newscore, stepsleftY,
                                                                    stepsleftO)
                            if result > best:
                                best = result
            if foundY and foundO:
                return best

        elif stepsYou!= 0 and stepsOllie != 0 and stepsYou<stepsOllie:
            current_path = path + [startYou] + [startOllie]
            foundY,foundO = False, False
            for toO, (distO, weightO) in self.distancegraph[startOllie].items():
                if toO not in current_path and distO < stepsOllie:
                    foundO = True
                    stepsleftO = stepsOllie - distO
                    testpath = current_path+ [toO]

                    for toy, (disty, weighty) in self.distancegraph[startYou].items():
                        if toy not in testpath and disty < stepsYou:
                            foundY = True
                            stepsleftY = stepsYou - disty
                            newscore = score + (weightO * (stepsOllie - distO)) + (weighty * (stepsYou -disty))
                            result = self.find_most_points_together(toy, toO, current_path, newscore, stepsleftY,
                                                                    stepsleftO)
                            if result > best:
                                best = result
            if foundY and foundO:
                return best


        elif stepsYou!= 0:
            current_path = path + [startYou]
            found = False
            for to,(dist,weight) in self.distancegraph[startYou].items():
                if to not in path and dist<stepsYou:
                    found = True
                    newscore = score + (weight * (stepsYou -dist))
                    stepsleftY = stepsYou - dist
                    result = self.find_most_points_together(to, startOllie, current_path, newscore,stepsleftY,stepsOllie)

                    if result > best:
                        best = result
            if found:
                return best

        elif stepsOllie != 0:
            current_path = path + [startOllie]
            found = False
            for to, (dist, weight) in self.distancegraph[startOllie].items():
                if to not in path and dist < stepsOllie:
                    found = True
                    newscore = score + (weight * (stepsOllie - dist))
                    stepsleftO = stepsOllie - dist
                    result = self.find_most_points_together(startYou, to, current_path, newscore, stepsYou,stepsleftO)
                    if result > best:
                        best = result
            if found:
                return best

        return best

start_time = time.time()
with open('2022-16Volcano.txt') as f:
    lines = f.read().splitlines()
    # print(lines)
    allnodes = []
    edges = []
    weigth = {}
    for line in lines:
        line = line.replace(",", "").replace(";", "").replace("=", " ").split(" ")
        allnodes.append(line[1])
        for i in range(10, len(line)):
            edges.append([line[i], line[1], int(line[5])])
        weigth[line[1]] = int(line[5])

    #optimize so it doesn't need to visit the 0 valves
    empties = []
    for node in weigth.items():
        if node[1] == 0:
            empties.append(node[0])

    ### PART 1 ###
    tunnelsystem = Graph(len(lines), True, allnodes, edges, weigth)
    start_time = time.time()
    print("Part 1: Releases:" ,tunnelsystem.find_most_points("AA", empties, 0, 30))
    print("part 1 took ", time.time() - start_time, " seconds to run")

    ### PART 2, COST 27 MINUTES TO RUN FOR WHOLE INPUT DATA###
    # start_time = time.time()
    # print(tunnelsystem.find_most_points_together("AA","AA", empties, 0, 26, 26))
    # print("empties took ", time.time() - start_time, " to run")

### BETTER SOLUTION for PART 2 (COST ABOUT 3,5 MINUTE)###
def split_valves(valves):
    rooms = {valve for valve in valves if valve != "AA"}

    size = len(rooms) // 2
    for me in itertools.combinations(sorted(rooms), size):
        yield set(me), rooms - set(me)

start_time = time.time()
tosearch = list(set(allnodes) - set(empties))
best = 0
for me, ollie in split_valves(tosearch):
    score = tunnelsystem.find_most_points_subgraph("AA", empties, 0, 26, me) + tunnelsystem.find_most_points_subgraph("AA", empties, 0, 26, ollie)
    if score > best:
        best = score
print("Part 2: releases",best)
print("Part 2 took ", time.time() - start_time, " seconds to run")


