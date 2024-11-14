import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


class Grid:
    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = [[c for c in row] for row in lines]
        self.directions = {"^": (-1, 0),
                           "v": (1, 0),
                           "<": (0, -1),
                           ">": (0, 1),
                           '.': [(0, 1), (0, -1), (-1, 0), (1, 0)]}
        self.start = (0, 1)
        self.finish = (self.height - 1, self.width - 2)

        # Part2 Graph
        self.graph = defaultdict(list)
        self.nodes = set()
        self.edges = defaultdict(list)
        self.build_graph()

    def printgrid(self):
        print("garden")
        for row in self.grid:
            print("".join("■" if cell == "#" else "." for cell in row))

    def is_valid(self, x, y, seen):
        return (0 <= x < self.width and
                0 <= y < self.height and
                self.grid[x][y] != '#' and
                (x,y) not in seen)

    def dfs(self,x,y,seen, length, slopes):
        max_length = 0

        if  (x,y) == self.finish:
            return length

        moves = []
        if slopes and self.grid[x][y] in '>^v<':
            moves.append(self.directions[self.grid[x][y]])
        else:
            moves.extend(self.directions['.'])

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny, seen):
                seen.add((nx, ny))
                max_length = max(max_length, self.dfs(nx, ny, seen, length+1, slopes))
                seen.remove((nx, ny))

        return max_length

    def find_longest_path(self, slopes = True):
        x, y = self.start
        seen = set()
        seen.add((x, y))
        return self.dfs(x,y,seen,0, slopes)

    def build_graph(self):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # ^>v<
        for y in range(self.width):
            for x in range(self.height):
                cell = self.grid[x][y]
                if cell != '#':  # If the current cell is not a wall
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:  # Check bounds
                            neighbour = self.grid[nx][ny]
                            if neighbour != '#':  # Add valid neighbors
                                self.graph[(x, y)].append((nx, ny))

        self.find_vertices_start_end()
        self.find_edges()

    def find_vertices_start_end(self):
        for (x, y), neighbours in self.graph.items():
            no_of_neighbours = len(neighbours)
            if no_of_neighbours != 2:  # Junctions or endpoints
                self.nodes.add((x, y))



    def find_edges(self):
        for node in self.nodes:
            queue = [(node, set())]

            while queue:
                (x, y), visited = queue.pop()

                for neighbour in self.graph[(x, y)]:
                    if neighbour not in visited:
                        if neighbour in self.nodes:
                            self.edges[node].append((neighbour, len(visited) + 1))
                        else:
                            queue.append((neighbour, visited | {(x, y)}))

    def find_longest_path_graph(self):
        path_distances = []
        queue = [(self.start, set(), 0)]

        while queue:
            (x, y), visited, distance = queue.pop()

            if (x, y) == self.finish:
                path_distances.append(distance)
                continue

            for neighbour_node, weight in self.edges[(x, y)]:
                if neighbour_node not in visited:
                    queue.append((neighbour_node, visited | {(x, y)}, distance + weight))

        if not path_distances:
            print("No path found from start to finish.")
            return 0

        return max(path_distances)




with open('2023-23-Long-Walk.txt') as f:
    lines = f.read().splitlines()

Maze = Grid(lines)
print("Part 1, Longest path is:", Maze.find_longest_path())

result = Maze.find_longest_path_graph()
print("Part 2, Longest path is:", result)

print("Part 2, Longest path is:", Maze.find_longest_path(False))

