import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from functools import lru_cache


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        for key, value in nodes.items():
            for v in value:
                self.edges.append((key, v))
        self.print_graph()

    def print_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.nodes.keys())
        G.add_edges_from(self.edges)

        colors = ["#4CAF50" if n == "you" else "#E53935" if n == "out" else "skyblue" for n in G.nodes()]
        plt.figure(figsize=(max(6, len(G.nodes()) * 0.1), max(4, len(G.nodes()) * 0.1)))



        nx.draw(G, with_labels=True, node_color=colors, node_size=1500, font_size=12, font_weight='bold',
                arrows=True, arrowsize=20)

        net = Network(height="1000px", width="100%", directed=True)
        net.from_nx(G)

        [n.update({"color":
                       {"background": "#4CAF50", "border": "#2E7D32"} if n["id"] in ["you", "svr"]
                       else {"background": "#E53935", "border": "#B71C1C"} if n["id"] in ["out"]
                       else {"background": "#FF9800", "border": "#E65100"} if n["id"] in ["dac", "fft"]
                       else {"background": "skyblue", "border": "#1E88E5"}
                   }) for n in net.nodes]

        [n.update({"size": 15}) for n in net.nodes]

        net.write_html("graph.html")

    @lru_cache(maxsize=None)
    def recursive_path_counter(self, pos, end):
        if pos == end:
            return 1

        total = 0
        for nxt in self.nodes[pos]:
            total += self.recursive_path_counter(nxt, end)
        return total

    @lru_cache(maxsize=None)
    def recursive_path_counter_visit(self, pos, end, visited_dac=False, visited_fft=None):
        if pos == end:
            if visited_dac and visited_fft:
                return 1
            else:
                return 0

        if pos == "dac":
            visited_dac = True

        if pos == "fft":
            visited_fft = True

        total = 0
        for nxt in self.nodes[pos]:
            total += self.recursive_path_counter_visit(nxt, end, visited_dac, visited_fft)
        return total

with open('2025-11-Reactor.txt') as f:
    lines = {
        k.strip(): v.strip().split()
        for k, v in (line.split(':', 1) for line in f.read().splitlines() if ':' in line)
    }
    ServerRack = Graph(lines)
    print("Part 1, number of paths is",ServerRack.recursive_path_counter("you", "out"))
    print("Part 2, number of paths is", ServerRack.recursive_path_counter_visit("svr", "out"))
