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
- day 6 - Lantern fish
  - For part 1 you need to fins out how big the school is after 80 days, this is done by using a dictionary which counts the fish for each times, then it loops over the days and sets als counts on the timer -1 and add for the 0 fish babys (on timer 8) and resets them by adding them to timer 6.
  - For part 2 you need to fins out how big the school is after 265 days, this is done the same as part one only for more days.
- day 7 - Whales
  - For part 1, you need to calculate the best horizontal alignment and the fuel spend for that
  - For part 2 you need to do the same, but the fuel spend is not a sum but a partial sum
- day 8 - Segment search
  - For part 1, you need to decipher screen digits, in part 1 you only need to do 1,4,7,8
  - For part 2 you need to decipher all screen digits
- day 9 - lava tube
  - For part 1 you need to find the lowest points and make the sum fo their risks
  - For part 2 you need to get the basins around the lowest point and get the multiplication or the size of the largest three
- day 10 - Syntax scoring
  - for part 1 you need to discard all the incomplete sentences and get the score of the wrong closing parentheses
  - for part 2 you need to discard all the wrong sentences and fill all the incomplete and calculate their score
- day 11 - Dumbo octopuses
  - for part 1 you need to count the number of flashes for 100 steps, octopuses flash when they have a value of 10, and when flashing give their neighbour one point up.
  - for part 2 you need to find out when all octopuses flash at the same time, so the algorithm is the same as before, but instead being a range the steps go till all flash at the same time.
- day 12 - Cave Graph
  - For part 1 you need to find all possible routes while finishing small caves only ones
  - For part 2 you need to find all possible routes but one of the small caves can be visited twice
- day 13 - Origami
  - For part 1 you need to fold a transparent paper (or matrix) one time and count the dots
  - For part 2 you need to do all the folds and count the remaining
- day 14 - Polymerization
  - For part 1 you need to calculate how many times each character is in a growing polymer of 10 steps
  - For part 2 you need to do 40 steps which makes it an optimalization problem
- day 15 - Chiton
  - For part 1 you need to find the least risk route through a cave(matrix), dijkstra is used.
  - For part 2 you need to make the matrix 5 times bigger for both sizes and use the same algorithm as 1
- day 16 - DecaHex decoder
  - For part 1 you need to translate all chars in hex to 4 digit binary and the get all sum of all the versions
  - For part 2 you need to get the value after using all the set conditions, which makes a massive recursive loop
- day 17 - Trick shot
  - For part 1 you need to find the aim to reach the highest Y, while landing in the range
  - For part 2 you need to find all aims working to land in the range
- day 18 - Snailfish math
  - For part 1 you need to calculate an addition the snailfish way and get the magnitude of the answer
  - For part 2 you need to find the highest number of any combination
- day 19 - Beacons
  - For part 1 you need to calculate how many beacons overlap, this is done by rotating the graph
  - For part 2 you need to find the largets manhatten distance between two scanners
- day 20 - Trench map
  - For part 1 you need enhance the image by getting a bit value, trick why the infinite does not work, it cause it changes value, with puzzle input
  - For part 2 you need to do the enhancing 50 times instead of 2 
- day 21 - Dirac dice
  - For part 1 play direc dice and score points with a deterministic dice
  - For part 2 play direc dice in many universes, so use a recursive add for wins

## Todo's
- day 17 --> is there a way to get rid of the hardcoded 1000

