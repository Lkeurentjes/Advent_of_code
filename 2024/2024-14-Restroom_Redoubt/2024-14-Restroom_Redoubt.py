import re
from colorama import Fore, Style

class Grid:
    def __init__(self, lines, width, height):
        self.start_positions = lines
        self.width = width
        self.height = height

    def simulate_walks(self, seconds):
        # calculate where robots are after seconds
        positions = []
        for x,y,dx,dy in self.start_positions:
            new_x = (x + dx * seconds) % self.width
            new_y = (y + dy * seconds) % self.height
            positions.append((new_x, new_y))
        return positions

    def count_quadrants(self, seconds):
        # count number of robots in quadrants and multiply
        mid_x = (self.width - 1) // 2
        mid_y = (self.height - 1) // 2

        QUADRANTS = [0,0,0,0]
        for x,y in self.simulate_walks(seconds):
            if x == mid_x or y == mid_y:
                continue  # Ignore robots exactly on the dividing lines
            elif x < mid_x and y < mid_y:
                QUADRANTS[0] += 1  # Top-left
            elif x >= mid_x and y < mid_y:
                QUADRANTS[1] += 1  # Top-right
            elif x < mid_x and y >= mid_y:
                QUADRANTS[2] += 1  # Bottom-left
            elif x >= mid_x and y >= mid_y:
                QUADRANTS[3] += 1  # Bottom-right

        return QUADRANTS[0] * QUADRANTS[1] * QUADRANTS[2] * QUADRANTS[3]

    def find_easter_egg(self):
        # find easter egg
        '''
        Based on assumption that Easter egg can be found when no robots overlap
        '''
        seconds = 0
        while True:
            seconds += 1

            positions = self.simulate_walks(seconds)
            if len(positions) == len(set(positions)):
                # self.display_pattern(positions)
                self.display_pattern_color(positions)
                return seconds



    def display_pattern(self, positions):
        # Create a grid to display the pattern
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for x, y in positions:
            grid[y][x] = "■"

        # Print the grid
        for row in grid:
            print("".join(row))

    def display_pattern_color(self, positions):
        # Create a grid to display the pattern but than with pretty colors
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for x, y in positions:
            grid[y][x] = "■"

        # Print the grid with borders and green #
        print("+" + "-" * self.width + "+")
        for row in grid:
            formatted_row = "".join(
                Fore.GREEN + cell + Style.RESET_ALL if cell == "■" else cell
                for cell in row
            )
            print(f"|{formatted_row}|")
        print("+" + "-" * self.width + "+")



with open('2024-14-Restroom_Redoubt.txt') as f:
    lines = [list(map(int, re.findall(r'-?\d+', line))) for line in f.read().splitlines()]
    # Map = Grid(lines, 11, 7)
    Map = Grid(lines, 101, 103)
    print("Part 1, muliplication of quadrants",Map.count_quadrants(100))
    print("Part 2, Easter egg:")
    seconds = Map.find_easter_egg()
    print("Can be found after", seconds, "seconds")
