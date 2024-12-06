# Advent of Code 2024
Advent of code 2024 solutions in python, using various algorithms.

## Kind of problems versus used algorithms

- day 1 - Hystorian Hysteria
    - For part 1, two list are sorted and total distance is calculated by taking the difference per pair
    - For part 2, the similarity score is calculated with the help of a counter map
- day 2 - Red nosed reports
    - For part 1, step size in list are checked on size and sign
    - For part 2, the list are also checked with one removed
- day 3 - Mull it over
    - For part 1, use a regex pattern to find all multiplications
    - For part 2, only do the multiplications when do() is before and not when don't() is before
- day 4 - Ceres search
    - For part 1, do word search puzzle of grid to find xmas
    - For part 2, instead of finding to word we need to find the x_mas pattern in grid
- day 5 - Print queue
    - For part 1, check if indexes order matches with rule and sum middle of the list
    - For part 2, reorder incorrect lists with help of a queue and a "directed" graph and sum the middle elements
- day 5 - Print queue
    - For part 1, Walk over grid and count visited cells
    - For part 2, Look for possible obstacles to make infinite loops


# todo
- part 2 day 6 is sort of brute force, just checking all the cells part 1 has visited