from collections import defaultdict
from itertools import combinations


class Grid:
    def __init__(self, lines):
        # Initialize the grid dimensions and data structures
        self.height = len(lines)
        self.width = len(lines[0])

        # Dictionary to store antennas based on their frequency
        self.antennas = defaultdict(list)
        self._get_antennas(lines)

        # Set to store unique antinode poisitions
        self.antinodes = set()

    def _get_antennas(self, grid):
        # Parse the grid to find antennas
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell != '.':  # Non-empty cells represent antennas
                    self.antennas[cell].append((x, y))

    def _on_map(self, x, y):
        # Check if (x, y) is on map
        return 0 <= x < self.width and 0 <= y < self.height

    def _extend_antinodes(self, x, y, dx, dy, start, times):
        # Extend antinode positions in a direction (dx, dy)
        for t in range(start, times):
            ax, ay = x + t * dx, y + t * dy
            if self._on_map(ax, ay):
                self.antinodes.add((ax, ay))
            else:
                return

    def find_antinodes(self, part2=False):
        # find antinodes for all antennas

        # Determine the number of steps for extending antinodes (only 1 for part 1)
        times_max = max(self.width, self.height) if part2 else 2
        times_start = 0 if part2 else 1

        # Iterate over each frequency and consider all pairs of antennas within frequency
        for freq, pos in self.antennas.items():
            for (x1, y1), (x2, y2) in combinations(pos, 2):
                dx, dy = x2 - x1, y2 - y1
                self._extend_antinodes(x1, y1, -dx, -dy, times_start, times_max)
                self._extend_antinodes(x2, y2, dx, dy, times_start, times_max)

        # Return the total count of unique antinodes
        return len(self.antinodes)


with open('2024-08-Resonant_Collinearity.txt') as f:
    lines = f.read().splitlines()
    Antennas = Grid(lines)
    print("Part 1, number of unique antinodes:", Antennas.find_antinodes())
    print("Part 2, number of unique antinodes:", Antennas.find_antinodes(True))
