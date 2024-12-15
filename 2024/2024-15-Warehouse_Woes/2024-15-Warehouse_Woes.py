import numpy as np


class Grid:
    def __init__(self, map):
        self.grid = np.array([list(row) for row in map])
        self.height, self.width = self.grid.shape

        # get info from the grid
        self.robot = tuple(np.argwhere(self.grid == '@')[0])
        self.walls = {tuple(pos) for pos in np.argwhere(self.grid == '#')}
        self.boxes = {tuple(pos) for pos in np.argwhere(self.grid == 'O')}
        self.boxesLeft, self.boxesRight = set(), set()  # needed for part 2

        self.moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    def step(self, direction):
        dx, dy = self.moves[direction]
        next_pos = (self.robot[0] + dx, self.robot[1] + dy)
        if next_pos in self.boxes:
            new_boxes = set()
            moving = True
            current_pos = next_pos

            while moving:
                next_box_pos = (current_pos[0] + dx, current_pos[1] + dy)
                if next_box_pos in self.walls:
                    moving = False
                elif next_box_pos not in self.boxes:
                    new_boxes.add(next_box_pos)
                    break
                else:
                    new_boxes.add(next_box_pos)
                    current_pos = next_box_pos

            if moving:
                for new_box in new_boxes:
                    self.boxes.remove((new_box[0] - dx, new_box[1] - dy))
                self.boxes.update(new_boxes)
                self.robot = next_pos

        elif next_pos not in self.walls:
            self.robot = next_pos

    def double_box_step(self, direction):
        dx, dy = self.moves[direction]
        next_pos = (self.robot[0] + dx, self.robot[1] + dy)

        if next_pos in self.boxesLeft or next_pos in self.boxesRight:
            new_boxes_left = set()
            new_boxes_right = set()

            current_check = set()
            if next_pos in self.boxesLeft:
                current_check.add(("L", next_pos))
                current_check.add(("R", (next_pos[0], next_pos[1] + 1)))
            if next_pos in self.boxesRight:
                current_check.add(("R", next_pos))
                current_check.add(("L", (next_pos[0], next_pos[1] - 1)))

            moving = True
            checked = set()

            while moving:
                free = True
                new_check = set()
                for side, (x, y) in current_check:
                    if (x, y) in checked:
                        continue
                    checked.add((x, y))
                    next_box_pos = (x + dx, y + dy)
                    if next_box_pos in self.walls:
                        moving = False
                        break
                    elif next_box_pos in self.boxesLeft:
                        free = False
                        new_check.add(("L", next_box_pos))
                        new_check.add(("R", (next_box_pos[0], next_box_pos[1] + 1)))
                    elif next_box_pos in self.boxesRight:
                        free = False
                        new_check.add(("R", next_box_pos))
                        new_check.add(("L", (next_box_pos[0], next_box_pos[1] - 1)))

                    if side == 'L':
                        new_boxes_left.add(next_box_pos)
                    if side == 'R':
                        new_boxes_right.add(next_box_pos)

                if free:
                    break
                else:
                    current_check = new_check

            if moving:
                for new_box in new_boxes_left:
                    self.boxesLeft.remove((new_box[0] - dx, new_box[1] - dy))
                self.boxesLeft.update(new_boxes_left)

                for new_box in new_boxes_right:
                    self.boxesRight.remove((new_box[0] - dx, new_box[1] - dy))
                self.boxesRight.update(new_boxes_right)

                self.robot = next_pos

        elif next_pos not in self.walls:
            self.robot = next_pos

    def walk(self, directions, part1=True):
        for direction in directions:
            (self.step if part1 else self.double_box_step)(direction)

    def calculate_gps_sum(self, part1=True):
        boxes = self.boxes if part1 else self.boxesLeft
        return sum(100 * x + y for x, y in boxes)

    def print_grid(self, part1=True):
        printgrid = np.full_like(self.grid, ".", dtype=str)

        if part1:
            for pos, char in {**{pos: '#' for pos in self.walls},
                              **{pos: 'O' for pos in self.boxes},
                              self.robot: '@'}.items():
                printgrid[pos] = char
        else:
            for pos, char in {**{pos: '#' for pos in self.walls},
                              **{pos: '[' for pos in self.boxesLeft},
                              **{pos: ']' for pos in self.boxesRight},
                              self.robot: '@'}.items():
                printgrid[pos] = char

        print("\n".join("".join(row) for row in printgrid))

    def scale_up_map(self):
        # Scale up the map width
        scaled_map = []
        scale_dict = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
        for row in self.grid:
            scaled_row = ''.join(scale_dict[cell] for cell in row)
            scaled_map.append(scaled_row)

        self.grid = np.array([list(row) for row in scaled_map])
        self.height, self.width = self.grid.shape
        self.robot = tuple(np.argwhere(self.grid == '@')[0])
        self.walls = {tuple(pos) for pos in np.argwhere(self.grid == '#')}
        self.boxesLeft = {tuple(pos) for pos in np.argwhere(self.grid == '[')}
        self.boxesRight = {tuple(pos) for pos in np.argwhere(self.grid == ']')}


with open('2024-15-Warehouse_Woes.txt') as f:
    map, directions = f.read().split("\n\n")
    Map = Grid(map.split("\n"))
    # Part One
    Map.walk(directions.replace("\n", ""))
    print("Part One GPS Sum:", Map.calculate_gps_sum())
    print("Based on grid:")
    Map.print_grid()

    # Part two
    print()
    Map.scale_up_map()
    Map.walk(directions.replace("\n", ""), False)
    print("Part Two GPS Sum:", Map.calculate_gps_sum(False))
    print("Based on grid:")
    Map.print_grid(False)
