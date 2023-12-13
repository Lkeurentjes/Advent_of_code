# Advent of Code 2023
Advent of code 2023 solutions in python, using various algorithms.

## Kind of problems versus used algorithms

- day 1 - calibration
    - For part 1 you need to find the first and last digit in a line and combine those, to get the sum of all lines.
    - For part 2 the digit can also be written in txt fromat, so with a little help form a dictionary I do the same.
- day 2 - color cubes
    - For part 1 you need to find out which games can be played with a set number of cubes and sum their id's
    - For part 2 you need to get the minimum numbers of cubes for each game and calculate the power of the total games, by summing up the color multiplication.
- day 3 - Gear Ratio's
  - For part 1 you need to find all numbers adjacent to a sign and use those
  - For part 2 you need to find all numbers adjacent to * and if it is exactly 2 multiply and sum those
- day 4 - Scratch cards
  - For part 1 you need to calculate all point won of a collection of scratch cards
  - For part 2 you need to calculate how many cards you end up with after winning
- day 5 - Food production problem
  - For part 1 you need to find the lowest number after you applied a bunch of translation based on ranges
  - For part 2 the seeds are not single seeds, but (in pairs) ranges of numbers, which makes it an optimalization problem. Instead of looping over the billions of seeds, I now split the ranges into (smaller) translated ranges and get the smallest range as smallest
- day 6 - Boat race
  - For part 1 you need to get the multiplication of all the possibilities to win
  - For part 2 you need to get the possibilities of one large race
- day 7 - Camel Poker
  - For part 1 you need to sort your cards upon poker score, and then the total score is the place of the card * the bid
  - For part 2 you need to do the same, but J are now Jokers, which can be any card, so you need to find the best replacement for the joker.
- day 8 - Dessert graph
  - For part 1 you need to find how long the route is from AAA to ZZZ, while following directions
  - For part 2 you need to find how many steps you need to take before all nodes ending on "A" are ending on "Z" at the same time, the least common multiple is used, to optimize
- day 9 - Mirage maintenance
  - For part 1 you need to calculate the next number before the sequence, with the use of a "pyramid"
  - For part 2 you need to calculate the number that came before the sequence the same way
- day 10 - pipe maze
  - For part 1, you need to calculate the farthest point from the startpoint while following the pipe
  - For part 2, you need to find how much of squares the pipe encloses
- day 11 - Cosmic expansion
  - For part 1 we get a universe, where all  rows or columns without stars need to get 2 times as big and then the shortest part between all stars needs to be summed
  - For part 2 we need to do the same, but multiply the empties bij 1000000
- day 12 - Hot springs
  - For part 1 you need to calculate the possible arrangement options for the groups in a string with known ("." or "#") an unknown places ("?")
  - For part 2 you need to do the same but the arrangement (+"?") and the groups get 5 times their size. Added cache to optimize the code
- day 13 - Point of Incidence
  - For part 1 you need to fins, where you can fold the map Horizontally or vertically
  - For part 2 you need to fins another fold where at you at most need to change 1 tile

## Todo's
