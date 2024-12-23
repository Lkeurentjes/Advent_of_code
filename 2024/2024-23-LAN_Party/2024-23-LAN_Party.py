from collections import defaultdict


class Graph:
    def __init__(self, lines):
        self.graph = defaultdict(set)
        for line in lines:
            self.graph[line[0]].add(line[1])
            self.graph[line[1]].add(line[0])
        self.triplets = self.find_tripelets()

    def find_tripelets(self):
        # Find and store all triplets (fully connected sets of 3 nodes)
        triplets = set()
        for node, neighbors in self.graph.items():
            # convert set to list for indexing
            neighbors = list(neighbors)
            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    # Check if neighbors are connected
                    if neighbors[j] in self.graph[neighbors[i]]:
                        triplet = tuple(sorted([node, neighbors[i], neighbors[j]]))
                        triplets.add(triplet)
        return triplets

    def filter_triplets(self, filter):
        # find all nodes that start with the filter string
        filtered_triplets = [triplet for triplet in self.triplets if any(node.startswith(filter) for node in triplet)]
        return filtered_triplets

    def find_largest_clique(self):
        # Bron–Kerbosch as helper algorithm
        def bron_kerbosch(current, candidates, processed, cliques):
            # Base case: No more candidates or processed vertices, meaning `current` is a maximal clique
            if not candidates and not processed:
                cliques.append(current)  # Add the maximal clique to the results
                return

            # Iterate through a copy of candidates (to modify the original set)
            for v in list(candidates):
                # Recursively build cliques including vertex v
                bron_kerbosch(
                    current.union({v}),  # Add v to the current clique
                    candidates.intersection(self.graph[v]),  # Filter candidates to v's neighbors
                    processed.intersection(self.graph[v]),  # Filter processed to v's neighbors
                    cliques  # Pass the cliques list for results
                )
                # Move vertex v from candidates to processed after exploring
                candidates.remove(v)
                processed.add(v)

        cliques = []
        bron_kerbosch(set(), set(self.graph.keys()), set(), cliques)
        largest_clique = max(cliques, key=len)

        return largest_clique

    def generate_password(self, clique):
        # make output for part 2
        return ','.join(sorted(clique))


with open('2024-23-LAN_Party.txt') as f:
    lines = [line.split("-") for line in f.read().splitlines()]
    Network = Graph(lines)
    # part 1
    print("Part 1, number of filtered tripelets ", len(Network.filter_triplets("t")))

    # Part 2
    largest_clique = Network.find_largest_clique()
    print("Part 2, Password to LAN Party:", Network.generate_password(largest_clique))
