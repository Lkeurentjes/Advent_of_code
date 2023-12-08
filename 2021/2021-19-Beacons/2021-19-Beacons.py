import math
import numpy as np


class Graph3D:
    def __init__(self, nodes):
        self.length = -1
        self.nodes = []
        self.distances = {}
        for n in nodes:
            self.add_node(n)

    def add_node(self, node):
        self.length += 1
        self.nodes.append(node)
        self.distances[self.length] = []

        def calculate_distance(node1, node2):
            # return math.sqrt(sum((x - y) ** 2 for x, y in zip(node1, node2)))
            return sum((x - y) ** 2 for x, y in zip(node1, node2))

        for key in self.distances:
            if key == self.length:
                break
            dist = calculate_distance(node, self.nodes[key])
            self.distances[self.length].append((key, dist))
            self.distances[key].append((self.length, dist))

    def printgraph(self):
        print("Nodes:", self.nodes)
        print("Distances:", self.distances)

    def get_rotation(self, other, same):
        target_points = [self.nodes[x[0]] for x in same]
        source_points = [other.nodes[x[1]] for x in same]

        # Step 1: Center the Point Clouds
        centroid_source = np.mean(source_points, axis=0)
        centroid_target = np.mean(target_points, axis=0)

        centered_source = source_points - centroid_source
        centered_target = target_points - centroid_target

        # Step 2: Compute the Covariance Matrix
        covariance_matrix = np.dot(centered_source.T, centered_target)

        # Step 3: Compute Singular Value Decomposition (SVD)
        U, _, Vt = np.linalg.svd(covariance_matrix)

        # Step 4: Calculate Rotation Matrix
        rotation_matrix = np.dot(Vt.T, U.T)

        # Ensure it's a proper rotation matrix
        if np.linalg.det(rotation_matrix) < 0:
            Vt[-1, :] *= -1
            rotation_matrix = np.dot(Vt.T, U.T)

        # Step 5: Calculate Translation Vector
        translation_vector = centroid_target - np.dot(rotation_matrix, centroid_source)

        return rotation_matrix, translation_vector

    def compare_isomorphic(self, other):
        same = []
        for i in range(self.length + 1):
            for j in range(other.length + 1):
                connections_self = set([x[1] for x in self.distances[i]])
                connections_other = set([x[1] for x in other.distances[j]])
                if len(connections_self.intersection(connections_other)) >= 11:
                    # print("\n")
                    # print(connections_self)
                    # print(connections_other)
                    # print(connections_self.intersection(connections_other))
                    same.append((i, j))

        if len(same) < 12:
            return False
        print(same)
        rotation, translation = self.get_rotation(other, same[:3])

        same_other = [x[1] for x in same]

        for i, node in enumerate(other.nodes):
            if not i in same_other:
                new = np.dot(rotation, np.array([node[0], node[1], node[2]]))
                new = new + translation
                self.add_node((self.proper_round(new[0]), self.proper_round(new[1]), self.proper_round(new[2])))
        return True

    def proper_round(self,num, dec=0):
        num = str(num)[:str(num).index('.')+dec+2]
        if num[-1]>='5':
            return int(float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1)))
        return int(float(num[:-1]))


with open('2021-19-Beacons.txt') as f:
    lines = f.read().split("\n\n")
    scanners = [[tuple(map(int, coord.split(','))) for coord in coords.split("\n")[1::]] for coords in lines]
    beacon_graphs = [Graph3D(nodes) for nodes in scanners]
    print(scanners)

def compare(beacon_graphs):
    for i, graphI in enumerate(beacon_graphs):
        for j, graphJ in enumerate(beacon_graphs[i+1::]):
            good = graphJ.compare_isomorphic(graphI)
            if good:
                beacon_graphs.pop(i)
                return beacon_graphs
    return beacon_graphs

while len(beacon_graphs) != 1:
    beacon_graphs = compare(beacon_graphs)
    print(len(beacon_graphs))

print(beacon_graphs[0].length + 1)
