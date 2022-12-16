from queue import Queue

class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed,nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = nodes
		
        # Directed or Undirected
        self.m_directed = directed
		
        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: [] for node in self.m_nodes}    
	
    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].append([node2, weight])

    
    # Print the graph representation
    def print_adj_list(self):
      for key in self.m_adj_list.keys():
        print("node", key, ": ", self.m_adj_list[key])
        
    def find_most_points(self,start, path, score,steps,edges):
        steps += 1
        if steps == 15:
            return score, path
            
        edgesCOPY = edges.copy()
        best_score = -1
        best_i = None
        best_path = None
    
        current_path = path + [start]
        for i in range(len(self.m_adj_list[start])):
            print(i)
            if not self.m_adj_list[start][i] in path:
                score_i, path_i = self.find_most_points(self.m_adj_list[start][i][0], current_path, score + self.m_adj_list[start][i][1],steps,edgesCOPY)
                if score_i > best_score:
                    best_score = score_i
                    best_i = i
                    best_path = path_i
        if best_i is None:
            return score, current_path
        else:
            return best_score, best_path
        


with open("1205input.txt") as f:
    lines = f.read().splitlines()
    allnodes = []
    edges = []
    for line in lines:
        line = line.replace(",","").replace(";","").replace("="," ").split(" ")
        allnodes.append(line[1])
        for i in range(10,len(line)):
            edges.append([line[i],line[1],int(line[5])])

    tunnelsystem = Graph(len(lines),True, allnodes)
    for edge in edges:
        tunnelsystem.add_edge(edge[0],edge[1],edge[2])
    tunnelsystem.print_adj_list()
    print(tunnelsystem.find_most_points("AA",[],0,0,tunnelsystem.m_adj_list))
