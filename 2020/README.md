# Advent of Code 2020

Advent of code 2020 solutions in python, using various algorithms.

## Kind of problems versus used algorithms

- day 1 - Report repair
    - For part 1, Two numbers are found using a set to efficiently identify pairs that sum to 2020, and their product is
      calculated.
    - For part 2, Three numbers are located by iterating over pairs and checking for a complement that completes the sum
      to 2020, and their product is computed.
- day 2 - Password Philosophy
    - For Part 1, The number of correct passwords is counted by ensuring the given character appears within the
      specified
      minimum and maximum range.
    - For Part 2, The number of correct passwords is determined by checking if the given character appears at exactly
      one of
      the two specified positions (1-indexed).
- day 3 - Toboggan Trajectory
    - For Part 1, The number of trees encountered is calculated by traversing the (infinite) grid with a slope of right
      3 and down 1.
    - For Part 2, The product of trees encountered is computed by traversing the (infinite) grid with multiple slopes
      and multiplying
      the results
- day 4 - passport processing
    - For Part 1, The number of valid passports is determined by checking if all required fields are present.
    - For Part 2, The number of valid passports is further refined by validating the values of each required field based
      on specific rules.
- day 5 - Binary Boarding
    - For Part 1, Each boarding pass encodes a seat using a binary space partitioning system. Using a recursive
      algorithm, the row and column of each seat are found, and the maximum seat ID is determined.
    - For Part 2, The IDs are sorted, and the missing ID (your seat) is located by identifying the gap in the sequence.