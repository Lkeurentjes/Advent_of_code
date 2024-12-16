import numpy as np
import heapq
from collections import deque

class Grid:
    def __init__(self, lines):
        self.grid = np.array([list(row) for row in lines])
        self.height, self.width = self.grid.shape

        self.start =  tuple(np.argwhere(self.grid == 'S')[0])
        self.end =  tuple(np.argwhere(self.grid == 'E')[0])

        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
        self.start_state = (self.start, 1)  # Start facing East (direction = 1)
        self.visited = {self.start_state: 0}

    def dijkstra(self):
        # Priority queue with initial cost and start state
        pq = [(0, self.start_state)]  # (cost, ((x, y), direction))

        while pq:
            cost, ((x, y), d) = heapq.heappop(pq)  # Get state with the lowest cost

            # Skip if this state has already been processed with a lower cost
            if self.visited.get(((x, y), d), float('inf')) < cost:
                continue

            # Move forward
            dx, dy = self.directions[d]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.height and 0 <= new_y < self.width and self.grid[new_x, new_y] != '#':
                new_cost = cost + 1  # Moving forward costs 1
                next_state = ((new_x, new_y), d)
                if new_cost < self.visited.get(next_state, float('inf')): # Skip if new cost is higher than before
                    self.visited[next_state] = new_cost
                    heapq.heappush(pq, (new_cost, next_state))

            # Turn left or right
            for nd in [(d - 1) % 4, (d + 1) % 4]:
                new_cost = cost + 1000  # Turning costs 1000
                next_state = ((x, y), nd)
                if new_cost < self.visited.get(next_state, float('inf')): # Skip if new cost is higher than before
                    self.visited[next_state] = new_cost
                    heapq.heappush(pq, (new_cost, next_state))

        # Return the minimum cost to reach the end point in any direction
        return min(self.visited[(self.end, d)] for d in range(4) if (self.end, d) in self.visited)

    def backtrack_shortest_paths(self):
        min_end_cost = self.dijkstra()

        on_shortest_path = set() # set for shortest path tiles
        q = deque() # Queue to process states for backtracking

        # Add all end states with the minimum cost to the queue
        for d in range(4):
            end = (self.end, d)
            if end in self.visited and self.visited[end] == min_end_cost:
                on_shortest_path.add(end)
                q.append(end)

        # Process the queue to backtrack the shortest path
        while q:
            (x, y), d = q.popleft()
            current_cost = self.visited[((x, y), d)]

            # Backtrack for forward moves
            dx, dy = self.directions[d]
            prev_x, prev_y = x - dx, y - dy
            if 0 <= prev_x < self.height and 0 <= prev_y < self.width and self.grid[prev_x, prev_y] != '#':
                prev_cost = current_cost - 1
                prev_state = ((prev_x, prev_y), d)
                if 0 <= prev_cost == self.visited[prev_state] and prev_state in self.visited:
                    if prev_state not in on_shortest_path: # Avoid reprocessing states
                        on_shortest_path.add(prev_state)
                        q.append(prev_state)

            # Backtrack for turns
            turn_cost = current_cost - 1000
            if turn_cost >= 0:
                for pd in [(d - 1) % 4, (d + 1) % 4]:
                    prev_state = ((x, y), pd)
                    if prev_state in self.visited and self.visited[prev_state] == turn_cost:
                        if prev_state not in on_shortest_path:
                            on_shortest_path.add(prev_state)
                            q.append(prev_state)

        # Return the number of unique tiles on the shortest path (and discard directions)
        return len({(x, y) for ((x, y), d) in on_shortest_path})

with open('2024-16-Reindeer_Maze.txt') as f:
    lines = f.read().splitlines()
    Maze = Grid(lines)
    print("Part 1: the lowest possible score is", Maze.dijkstra())
    print("Part 2: number of tiles for the cheapest path", Maze.backtrack_shortest_paths())
