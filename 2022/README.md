# Advent of code 2022
 Advent of code 2022 solutions in python, using various algorithms.

## Kind of problems versus used algorithms

- day 1 - calorie counting
  - For part 1 you need to find the elf carrying the most calories, which is done by looping over the elves and summing up the calories, after that the sums are used to find the max
  - For part 2 you need to find the three elves carrying the most calories, which is done by looping over the elves and adding the total per elf top a new list, which is the sorted. The first three are summed together after that.
- day 2 - Rock, Paper, Scissors
  - For Part 1 you need to calculate the total score of the game according to a strategy, this is done by making a dictionary with points for each outcome and the loop over the outcomes and translate them into scores which are summed.
  - For part 2 you need to do the same, but with a different score, so another dictionary is used
- day 23 - Plant the starfruit
  - For part 1 all elves need to move using the given considerations per elf, in the end you need to calculate the empty ground in the boundingbox of the elves
  - For Part 2 you need to find after which round the elves are spread out enough, seeing they dont move anymore
- day 24 - Blizard Basin
  - For part 1 you need to fins the fastest route to the end, while not getting hit or moving into a blizzard
  - For part 2 you need to do the same but find the fastest route for going to the end, back to the start, back to the end.
- day 25 - Hot air balloon
  - For Part 1 You need to translate a list from SNAFU sum those and give your answer translated back from SNAFU

## Todo's
- 14, optimize part 2
- 15, optimize part 2
- 17, doesn't work
- 22 part 2
- 25

