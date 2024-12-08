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

# todo

- part 2 day 6 is sort of brute force, just checking all the cells part 1 has visited