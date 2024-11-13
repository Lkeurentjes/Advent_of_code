import numpy as np
import itertools
import z3

class Storm:
    def __init__(self, lines):
        self.testmin = 200000000000000
        self.testmax = 400000000000000

        self.hailstones2D = []
        self.hailstones3D = []
        for line in lines:
            numbers_str = line.replace('@', ',').split(',')
            numbers = [int(num.strip()) for num in numbers_str if num.strip()]
            self.hailstones3D.append(numbers)
            numbers2d = [numbers[i] for i in [0, 1, 3, 4]]
            self.hailstones2D.append(numbers2d)

        self.Intersections2D = 0

    def storm2d(self):
        for v1, v2 in itertools.combinations(self.hailstones2D, 2):
            if self.intersect2d(v1, v2):
                self.Intersections2D += 1

        return self.Intersections2D

    def intersect2d(self,v1,v2):
        # Extract components
        x1, y1, dx1, dy1 = v1
        x2, y2, dx2, dy2 = v2

        # Formulate the linear system Ax = B
        A = np.array([[dx1, -dx2], [dy1, -dy2]])
        B = np.array([x2 - x1, y2 - y1])

        try:
            # Solve for t1 and t2
            t1, t2 = np.linalg.solve(A, B)
        except np.linalg.LinAlgError:
            # If determinant is zero, lines are parallel or coincident
            return False

        # Check if both t1 and t2 are non-negative
        if t1 < 0 or t2 < 0:
            return False

        # Calculate the intersection point
        intersection_x = x1 + t1 * dx1
        intersection_y = y1 + t1 * dy1

        # Check if the intersection is within the window
        if not (self.testmin <= intersection_x <= self.testmax and self.testmin <= intersection_y <= self.testmax):
            return False

        # The vectors intersect within the window
        return True

    def rock_solver(self):
        x, y, z, dx, dy, dz, t0, t1, t2 = z3.Reals("x y z dx dy dz t0 t1 t2")

        # use first 3 asume it works for all, seeing one line:
        x0, y0, z0, dx0, dy0, dz0 = self.hailstones3D[0]
        x1, y1, z1, dx1, dy1, dz1 = self.hailstones3D[1]
        x2, y2, z2, dx2, dy2, dz2 = self.hailstones3D[2]

        # equation
        equations = [
            x + t0 * dx == x0 + t0 * dx0,
            y + t0 * dy == y0 + t0 * dy0,
            z + t0 * dz == z0 + t0 * dz0,
            x + t1 * dx == x1 + t1 * dx1,
            y + t1 * dy == y1 + t1 * dy1,
            z + t1 * dz == z1 + t1 * dz1,
            x + t2 * dx == x2 + t2 * dx2,
            y + t2 * dy == y2 + t2 * dy2,
            z + t2 * dz == z2 + t2 * dz2,
            ]

        # solve
        s = z3.Solver() # Create a Z3 solver instance
        s.add(equations) # Add the constraints
        s.check() #check if solution exsist
        r = s.model() #model the solution
        return sum(r[x].as_long() for x in [x, y, z])


with open('2023-24-Never-tell-me-the-odds.txt') as f:
    lines = f.read().splitlines()

Hailstorm = Storm(lines)
print("Part 1, Number of intersections is:", Hailstorm.storm2d())
print("Part 2, Sum of initial position components:", Hailstorm.rock_solver())