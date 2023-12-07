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
            return round(math.sqrt(sum((x - y) ** 2 for x, y in zip(node1, node2))),0)

        for key in self.distances:
            if key == self.length:
                break
            dist = calculate_distance(node,self.nodes[key])
            self.distances[self.length].append((key, dist))
            self.distances[key].append((self.length, dist))

    def printgraph(self):
        print("Nodes:", self.nodes)
        print("Distances:", self.distances)

    def get_rotation(self,other,same):
        print("ROTATION",same)
        source_points = [self.nodes[x[0]] for x in same]
        target_points = [other.nodes[x[1]] for x in same]

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
        print("\n")
        self.printgraph()
        other.printgraph()

        same = []
        for i in range(self.length+1):
            for j in range(other.length+1):
                connections_zero_self = set([x[1] for x in self.distances[i]])
                connections_zero_other = set([x[1] for x in other.distances[j]])
                if len(connections_zero_self.intersection(connections_zero_other)) >= 11:
                    same.append((i,j))
        print(same)
        if len(same) < 12:
            return True

        rotation, translation = self.get_rotation(other, same[:3])
        print(rotation)
        print(translation)

        #0 1 3 4 5 6 7 9 12 14 19 24
        return True



with open('2021-19-Beacons.txt') as f:
    lines = f.read().split("\n\n")
    scanners = [[tuple(map(int, coord.split(','))) for coord in coords.split("\n")[1::]] for coords in lines]
    beacon_graphs = [Graph3D(nodes) for nodes in scanners]
    print(scanners)

start_graph = beacon_graphs.pop(0)
while len(beacon_graphs) != 0:
    for i, graph in enumerate(beacon_graphs):
        good = start_graph.compare_isomorphic(graph)
        if good:
            beacon_graphs.pop(i)
            break
