import numpy as np


class Grid:
    def __init__(self, image, alg):
        self.algorithm = alg
        self.image = np.array([[1 if char == '#' else 0 for char in row] for row in image])
        self.infinite_value = 0  # Infinite region starts as dark

    def print_grid(self):
        for row in self.image:
            print("".join("■" if cell == 1 else "." for cell in row))

    def get_bit(self, x, y):
        cells = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 0), (0, 1),
                 (1, -1), (1, 0), (1, 1)]

        bit = ""
        for dx, dy in cells:
            if 0 <= x + dx < self.image.shape[0] and 0 <= y + dy < self.image.shape[1]:
                bit += str(int(self.image[x + dx][y + dy]))
            else:
                bit += str(self.infinite_value)  # Use infinite value for out-of-bounds
        return int(bit, 2)

    def enhance_grid(self):
        self.image = np.pad(self.image, pad_width=1, mode='constant', constant_values=self.infinite_value)

        new_image = np.zeros_like(self.image)
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                index = self.get_bit(x, y)
                if self.algorithm[index] == "#":
                    new_image[x][y] = 1

        self.image = new_image

        # Update the infinite value based on the algorithm
        if self.infinite_value == 0:
            self.infinite_value = 1 if self.algorithm[0] == "#" else 0
        else:
            self.infinite_value = 1 if self.algorithm[-1] == "#" else 0


    def Enhance(self, times):
        for i in range(times):
            self.enhance_grid()
        return int(np.sum(self.image))


with open('2021-20-Trench_map.txt') as f:
    lines = f.read().splitlines()
    enhancement_alg = lines[0]
    image = lines[2::]

Image = Grid(image, enhancement_alg)
print("Part 1, lit pixels are", Image.Enhance(2))
# 48 cause 50-2
print("Part 2, lit pixels are", Image.Enhance(48))
