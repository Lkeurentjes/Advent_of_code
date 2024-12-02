import math
import numpy as np
from itertools import product, permutations


class Graph3D:
    def __init__(self, nodes):
        self.nodes = set(nodes)

    def add_node(self, node):
        rounded_node = tuple(round(coord) for coord in node)
        self.nodes.add(rounded_node)

    def get_rotations(self):
        rotations = []
        for perm in permutations([0, 1, 2]):
            for signs in product([-1, 1], repeat=3):
                def rotate(node, perm=perm, signs=signs):
                    return [
                        node[perm[0]] * signs[0],
                        node[perm[1]] * signs[1],
                        node[perm[2]] * signs[2],
                    ]
                rotations.append(rotate)
        return rotations

    def align_with(self, other):
        rotations = other.get_rotations()
        for rotate in rotations:
            rotated_nodes = {tuple(rotate(node)) for node in other.nodes}
            for self_node in self.nodes:
                for other_node in rotated_nodes:
                    translation = tuple(self_node[i] - other_node[i] for i in range(3))
                    translated_nodes = {tuple(node[i] + translation[i] for i in range(3)) for node in rotated_nodes}
                    overlap = self.nodes & translated_nodes
                    if len(overlap) >= 12:
                        return translated_nodes, translation
        return None, None


def assemble_graph(scanners):
    graphs = [Graph3D(nodes) for nodes in scanners]

    assembled = graphs.pop(0)
    print(len(assembled.nodes))
    scanner_positions = [(0, 0, 0)]

    while graphs:
        for i, graph in enumerate(graphs):
            rotated_nodes, translation = assembled.align_with(graph)
            if rotated_nodes:
                for node in rotated_nodes:
                    assembled.add_node(node)
                scanner_positions.append(translation)
                graphs.pop(i)
                print("Overlap found, new number of beacons is",len(assembled.nodes))
                break
            else:
                print("No overlap now between base and scanner")
    return assembled.nodes, scanner_positions

def largest_manhattan_distance(scanner_positions):
    max_distance = 0
    for i in range(len(scanner_positions)):
        for j in range(i + 1, len(scanner_positions)):
            dist = sum(abs(scanner_positions[i][k] - scanner_positions[j][k]) for k in range(3))
            max_distance = max(max_distance, dist)
    return max_distance

with open('2021-19-Beacons.txt') as f:
    lines = f.read().split("\n\n")
    scanners = [[tuple(map(int, coord.split(','))) for coord in coords.split("\n")[1::]] for coords in lines]

beacons, scanner_positions = assemble_graph(scanners)
print("Part 1, Number of unique beacons:", len(beacons))
print("Part 2, Maximum distance of beacons is:", largest_manhattan_distance(scanner_positions))

