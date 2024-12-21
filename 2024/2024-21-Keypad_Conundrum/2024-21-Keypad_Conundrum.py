import numpy as np
from functools import lru_cache
from itertools import permutations


class Keypads:
    def __init__(self):
        # Define the keypads
        self.numeric_keypad = np.array([
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            [' ', '0', 'A']
        ])

        self.directional_keypad = np.array([
            [' ', '^', 'A'],
            ['<', 'v', '>']
        ])

        self.start = "A"
        self.directions = {(-1, 0): "^", (1, 0): 'v', (0, -1): '<', (0, 1): '>'}
        self.reverse_directions = {v: k for k, v in self.directions.items()}  # Reverse mapping

    def is_safe(self, x, y, num=True):
        keypad = self.numeric_keypad if num else self.directional_keypad
        return (
                0 <= x < len(keypad) and
                0 <= y < len(keypad[0]) and
                keypad[x][y] != " "
        )

    @lru_cache(maxsize=None)  # use lru cache to cache known results to be reused
    def All_paths(self, startchar, endchar, num=True):
        if startchar == endchar:
            return {"A"}

        keypad = self.numeric_keypad if num else self.directional_keypad
        start = tuple(np.argwhere(keypad == startchar)[0])
        end = tuple(np.argwhere(keypad == endchar)[0])

        # path consists of
        path = ""
        dx = start[0] - end[0]
        path = path + "v" * abs(dx) if dx < 0 else path + "^" * abs(dx)
        dy = start[1] - end[1]
        path = path + ">" * abs(dy) if dy < 0 else path + "<" * abs(dy)

        # return correct paths
        correct_options = set()
        for p in permutations(path):
            # check that paths doesn't cross the gap
            valid = True
            cur_x, cur_y = start
            for step in p:
                dx, dy = self.reverse_directions[step]
                cur_x += dx
                cur_y += dy
                if not self.is_safe(cur_x, cur_y, num=num):
                    # crossed the Gap
                    valid = False
                    break
            if valid:
                # didn't cross the gap
                correct_options.add("".join(p) + "A")
        return correct_options

    @lru_cache(maxsize=None)  # use lru cache to cache known results to be reused
    def shortest_end_path(self, code, depth, maxdepth):
        num = True if depth == 1 else False # to know which keyboard is used

        total_length = 0
        startchar = self.start

        for char in code:
            # find all possible paths
            path_options = self.All_paths(startchar, char, num=num)

            if depth == maxdepth:
                # add minimal length
                total_length += len(min(path_options, key=len))
            else:
                # find minimal length of next depth
                lengths = set()
                for path_option in path_options:
                    lengths.add(self.shortest_end_path(path_option, depth + 1, maxdepth))
                total_length += min(lengths)

            # next char
            startchar = char

        return total_length

    def calculate_compexity(self, code, maxdepth):
        # Calculate complexity
        number = int(''.join(filter(str.isdigit, code)))
        length = self.shortest_end_path(code, 1, maxdepth)
        return length, number


with open('2024-21-Keypad_Conundrum.txt') as f:
    codes = f.read().splitlines()
    Keyboards = Keypads()
    total_complexity, total_complexity25 = 0, 0

    for code in codes:
        # 3 robots (1 on numeric keyboards, 2 on directional)
        sequence_length, numeric_part = Keyboards.calculate_compexity(code, 3)
        total_complexity += sequence_length * numeric_part

        # 26 robots (1 on numeric keyboards, 25 on directional)
        sequence_length, numeric_part = Keyboards.calculate_compexity(code, 26)
        total_complexity25 += sequence_length * numeric_part

    print("Part 1, has a total complexity of", total_complexity)
    print("Part 2, has a total complexity of", total_complexity25)
