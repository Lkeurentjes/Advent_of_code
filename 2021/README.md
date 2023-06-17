# Advent of code 2021
 Advent of code 2021 solutions in python, using various algorithms.

## Kind of problems versus used algorithms

- day 1 - Sonar Sweep
  - For part 1 you need to find out how many times the depth increases, which is done by looping over the depth and when the next is bigger, it increases the counter
  - For part 2 you need to find out how many times the sum of three depth increases, which is done by looping over the depth with use of a range and when the sums next are bigger, it increases the counter
- day 2 - Dive
  - For part 1 you need to find the end position of the submarine after the planned course. This is done by sums and substractions of the course.
  - For part 2 you need to find the end position of the submarine after the planned course, but depth is now decided on aim. This is done by sums and substractions and multiplications of the course.
- day 3 - Binary Diagnostic
  - For part 1 you need to find 2 rates based on most common and least common bits. This is done by looping over the bits with a count function.
  - For Part 2 you need to find 2 rates based on most common and least common, but after choosing a number, the other binaries dissapear. This is done by a count function and removing the numbers not used anymore from the list.
- day 5 - Hydrothermal Venture
  - For Part 1 you need to find density of vents in a grid (considering only horizontal and vertical), this is done by making a np zeros matrix as grid and project the vents onto the grid by making the grid value +=1. The "too dense" points are the calculated with the np where function.
  - For Part 2 you need to find density of vents in a grid (also considering the diagonal vents), this is done by making a np zeros matrix as grid and project the vents onto the grid by making the grid value +=1. The "too dense" points are the calculated with the np where function.

  - 

## Todo's


