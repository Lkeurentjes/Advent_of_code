import numpy as np

class Grid:
    def __init__(self, lines):
        self.keys, self.locks = [], []
        for grid in lines:
            matrix = np.array([list(row) for row in grid.split('\n')])
            code = (np.sum(matrix == '#', axis=0) - 1).tolist()
            if np.all(matrix[0] == '#'):
                # Lock
                self.locks.append(code)
            else:
                # Key
                self.keys.append(code)


    def test_combinations(self):
        counter = 0
        for lock in self.locks:
            for key in self.keys:
                counter += all(l + k < 6 for l, k in zip(lock, key))
        return counter


with open('2024-25-Code_Chronicle.txt') as f:
    lines = f.read().split("\n\n")
    KeyLock = Grid(lines)
    print("Part 1, number of possibilities", KeyLock.test_combinations())

