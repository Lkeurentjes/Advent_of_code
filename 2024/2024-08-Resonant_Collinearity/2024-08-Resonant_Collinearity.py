from collections import defaultdict
from itertools import combinations

class Grid:
    def __init__(self, lines):
        """Initialize the grid with dimensions, antennas, and data structures."""
        self.height = len(lines)
        self.width = len(lines[0])

        # Store antenna positions grouped by their frequency
        self.antennas = defaultdict(list)
        self._parse_antennas(lines)

        # Set to store unique antinode positions
        self.antinodes = set()

    def _parse_antennas(self, grid):
        """Parse the grid to find and record antennas."""
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell != '.':
                    self.antennas[cell].append((x, y))

    def _is_within_bounds(self, x, y):
        """Check if a coordinate is within the bounds of the grid."""
        return 0 <= x < self.width and 0 <= y < self.height

    def _extend_antinode_positions(self, x, y, dx, dy, start, steps):
        """Extend antinode positions in a given direction."""
        for step in range(start, steps):
            new_x, new_y = x + step * dx, y + step * dy
            if self._is_within_bounds(new_x, new_y):
                self.antinodes.add((new_x, new_y))
            else:
                break

    def find_antinodes(self, part2=False):
        """Find and count unique antinode positions based on antenna placement."""
        max_steps = max(self.width, self.height) if part2 else 2
        start_step = 0 if part2 else 1

        # Iterate over each frequency and compute antinodes for antenna pairs
        for freq, positions in self.antennas.items():
            for (x1, y1), (x2, y2) in combinations(positions, 2):
                dx, dy = x2 - x1, y2 - y1

                # Extend antinode positions in both directions
                self._extend_antinode_positions(x1, y1, -dx, -dy, start_step, max_steps)
                self._extend_antinode_positions(x2, y2, dx, dy, start_step, max_steps)

        return len(self.antinodes)

if __name__ == "__main__":
    # Read input and process the grid
    with open('2024-08-Resonant_Collinearity.txt') as file:
        lines = file.read().splitlines()

    antennas = Grid(lines)

    # Output results for both parts
    print("Part 1, number of unique antinodes:", antennas.find_antinodes())
    print("Part 2, number of unique antinodes:", antennas.find_antinodes(part2=True))
