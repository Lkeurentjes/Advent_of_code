def coord_exsist(x, y, max_x, max_y):
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return False
    return True


def found_xmas(x, y, dir, grid, word="XMAS"):
    for i in range(len(word)):
        new_x, new_y = x + i * dir[0], y + i * dir[1]

        # check if coord exsist
        if not coord_exsist(new_x, new_y, len(grid), len(grid[0])):
            return False

        # check if letter is not incorrect
        if grid[new_x][new_y] != word[i]:
            return False

    return True


def count_xmas(grid, word="XMAS"):
    count = 0

    # all possible directions in word search
    directions = [
        (0, 1),  # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    # Iterate through the grid
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dir in directions:
                if found_xmas(x, y, dir, grid, word):
                    count += 1

    return count


def found_x_mas(x, y, pattern, grid):
    for char, dx, dy in pattern:
        new_x, new_y = x + dx, y + dy

        # check if coord exsist
        if not coord_exsist(new_x, new_y, len(grid), len(grid[0])):
            return False

        # check if letter is not incorrect
        if grid[new_x][new_y] != char:
            return False

    return True


def count_x_mas(grid):
    count = 0

    # Possible X-MAS patterns
    patterns = [
        [('M', -1, -1), ('S', -1, 1), ('A', 0, 0), ('M', 1, -1), ('S', 1, 1)],  # Original
        [('S', -1, -1), ('M', 1, -1), ('A', 0, 0), ('S', -1, 1), ('M', 1, 1)],  # Rotated 90
        [('S', 1, -1), ('M', 1, 1), ('A', 0, 0), ('S', -1, -1), ('M', -1, 1)],  # Rotated 180
        [('M', -1, 1), ('S', 1, 1), ('A', 0, 0), ('M', -1, -1), ('S', 1, -1)]  # Rotated 270
    ]

    # Iterate through the grid
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for pattern in patterns:
                if found_x_mas(x, y, pattern, grid):
                    count += 1

    return count

with open('2024-04-Ceres_Search.txt') as f:
    lines = f.read().splitlines()

print("Part 1, total occurrences of XMAS:", count_xmas(lines))
print("Part 2, total occurrences of X-MAS:", count_x_mas(lines))
