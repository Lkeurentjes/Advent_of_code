# Advent of Code 2024

Advent of code 2024 solutions in python, using various algorithms.

## Kind of problems versus used algorithms

- Day 1 - Hystorian Hysteria
    - For part 1, two list are sorted and total distance is calculated by taking the difference per pair
    - For part 2, the similarity score is calculated with the help of a counter map
- Day 2 - Red nosed reports
    - For part 1, step size in list are checked on size and sign
    - For part 2, the list are also checked with one removed
- Day 3 - Mull it over
    - For part 1, use a regex pattern to find all multiplications
    - For part 2, only do the multiplications when do() is before and not when don't() is before
- Day 4 - Ceres search
    - For part 1, do word search puzzle of grid to find xmas
    - For part 2, instead of finding to word we need to find the x_mas pattern in grid
- Day 5 - Print queue
    - For part 1, check if indexes order matches with rule and sum middle of the list
    - For part 2, reorder incorrect lists with help of a queue and a "directed" graph and sum the middle elements
- Day 6 - Print queue
    - For part 1, Walk over grid and count visited cells
    - For part 2, Look for possible obstacles to make infinite loops
- Day 7 - Bridge repair
    - For part 1, check if result can be achieved by sum or multiplications and take sum of total
    - For part 2, add concatenation as option to make true and take sum of total
- Day 8 - Resonant collinearity
    - For part 1, the number of unique antinodes based on the resonant frequencies of the antennas in grid needs to be
      found
    - For part 2, the number of unique antinodes based on effects of resonant harmonics needs to be found
- Day 9 - Disk fragmenter
    - For part 1, we need to order the disk as compact as possible and doe a checksum
    - For part 2, we only need to move when space is big enough
- Day 10 - Hoof It
    - For part 1, the number of distinct 9-height positions reachable from each 0-height trailhead is calculated using a
      breadth-first search (BFS), and their sum is taken as the result.
    - For part 2, the number of distinct hiking trails starting at each 0-height trailhead is counted by propagating
      trail paths through BFS, and their sum is taken as the result.
- Day 11 - Plutonian pebbles
    - For part 1, the total number of stones after 25 "blinks" is calculated by applying transformations based on the
      rules for splitting, multiplying, or replacing stones.
    - For part 2, the total number of stones after 75 "blinks" is calculated in the same manner, using a Counter instead
      of transforming the list is needed for efficiency.
- Day 12 - Garden Groups
    - For part 1, walk over the garden grid using BFS to determine connected plots of the same type. Calculate the
      area and perimeter of each plot, summing the product of these values for all plots.
    - For part 2, extend the BFS logic to include the calculation of corners (sides) for each plot and sum the
      product of area and sides for all plots.
- Day 13 - Claw Contraption
    - For part 1, use a brute force method or Z3 SMT solver to calculate the minimum tokens required to match the
      target position using two types of moves, subject to constraints on maximum button presses.
    - For part 2, solve the same problem with an added offset to the target position, efficiently handled by the Z3
      SMT solver.
- Day 14 - Restroom Redoubt
    - For part 1, simulate the movement of robots over a grid for a given time to calculate the number of robots in each
      quadrant. Multiply the counts of robots in all four quadrants for the result.
    - For part 2, identify the first time step when no robots overlap on the grid, and display the resulting pattern
      visually with colors to reveal the "Easter egg".
- Day 15 - Warehouse Woes
    - For part 1, simulate a robot pushing boxes on a grid based on directional instructions. Calculate the sum of GPS
      coordinates for all boxes in their final positions.
    - For part 2, expand the grid and implement a double-box handling mechanism. Simulate movements and calculate the
      updated GPS sum for all boxes, including scaled-up representations.
- Day 16 - Reindeer Maze
    - For part 1, implement Dijkstra's algorithm to find the lowest possible cost to navigate a maze, considering the
      cost of movement and turning.
    - For part 2, backtrack through the shortest paths to determine the number of unique tiles visited in the cheapest
      route, ensuring all possible directions are accounted for.
- Day 17 - Chronospatial Computer
    - For part 1, simulate a program execution based on opcodes and a set of registers, producing the program's output
      based on specified rules.
    - For part 2, identify the smallest possible value of register A that reproduces the program's output through
      backtracking and testing ranges efficiently.
- Day 18 - RAM Run
    - For part 1, use BFS to determine the minimum steps required to traverse from the start to the exit in a grid. The
      grid's corruption state impacts' traversal.
    - For part 2, analyze the grid's connected components to identify the point where the path becomes impossible, based
      on memory corruption patterns.
- Day 19 - Linen Layout
    - For part 1, count the number of designs that can be fully constructed using a set of towel patterns.
    - For part 2, calculate the total number of arrangements possible for each design, using recursive memoization to
      efficiently compute all valid combinations.
- Day 20 - Race Condition
    - For part 1, implement Dijkstra's algorithm to calculate the shortest path from the start to the end of a maze.
      Identify areas where the maximum difference between adjacent tiles exceeds 100.
    - For part 2, extend the analysis to include jumps of maximum range 20. Count the occurrences where jumps
      result in a maximum difference exceeding 100.
- Day 21 - Keypad Conundrum
    - For part 1, determine all possible paths through a numeric keypad, ensuring that movements do not cross invalid
      gaps. Calculate the total complexity for given codes based on these constraints.
    - For part 2, extend the complexity calculations to include additional keypads with directional controls. Analyze
      the total complexity using multiple robots to navigate both keypads.
- Day 22 - Monkey Market
    - For part 1, simulate a sequence of transformations on secrets using bitwise and modular operations to generate
      final values. Sum these values for a given number of iterations.
    - For part 2, analyze price changes and find the most profitable sequence of consecutive changes. Identify the best
      sequence to sell based on a scoring system using patterns in price changes.
- Day 23 - LAN Party
    - For part 1, identify fully connected triplets of nodes in a network graph. Filter these triplets based on a given
      prefix and count their occurrences.
    - For part 2, find the largest clique in the network graph using the Bron–Kerbosch algorithm. Generate a password
      based on the sorted nodes in this largest clique.
- Day 24 Crossed wires
- Day 25 Code Chronicle
    - For part 1, identify keys and locks from grids and find which do not overlap

# todo

- part 2 day 6 is sort of brute force, just checking all the cells part 1 has visited