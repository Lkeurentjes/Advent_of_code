import re
from itertools import product
from z3 import *


def min_tokens_needed(dx1, dy1, dx2, dy2, x, y, max_pushes=100):
    # Check all combinations of A and B presses NB: only usable if max pushes is smallisch
    min_tokens = float('inf')
    best_solution = None

    for a_presses, b_presses in product(range(max_pushes + 1), repeat=2):
        # Calculate the resulting X and Y positions
        x_pos = a_presses * dx1 + b_presses * dx2
        y_pos = a_presses * dy1 + b_presses * dy2

        # Check if the positions match the prize's position
        if x_pos == x and y_pos == y:
            # Calculate the token cost
            tokens = a_presses * 3 + b_presses

            # Update the minimum token solution
            if tokens < min_tokens:
                min_tokens = tokens
                best_solution = (min_tokens, a_presses, b_presses)

    return best_solution


def min_tokens_z3(dx1, dy1, dx2, dy2, x, y, add=0, max_pushes=None):
    """Solve using Z3 SMT Solver."""
    # Define variables for button presses which need to be solved
    a = Int('a')  # Presses for Button A
    b = Int('b')  # Presses for Button B

    # initialize solver
    solver = Solver()

    # add constraints
    solver.add(dx1 * a + dx2 * b == x + add)  # add for part 2
    solver.add(dy1 * a + dy2 * b == y + add)  # add for part 2
    solver.add(a >= 0)  # pushes can not be negative
    solver.add(b >= 0)  # pushes can not be negative

    if max_pushes:
        # extra constraint for part 1
        solver.add(a <= max_pushes)
        solver.add(b <= max_pushes)

    solutions = (float('inf'), None, None)
    while solver.check() == sat:
        solution = solver.model()
        a_val = solution[a].as_long()
        b_val = solution[b].as_long()
        tokens = 3 * a_val + b_val

        if tokens < solutions[0]:
            solutions = (tokens, a_val, b_val)

        # Block the current solution
        solver.add(Or(a != a_val, b != b_val))

    if solutions[1]:
        # print(f"Solution found: Tokens={tokens}, A={a_val}, B={b_val}")
        return solutions


with open('2024-13-Claw_Contraption.txt') as f:
    lines = [list(map(int, re.findall(r'\d+', line))) for line in f.read().split("\n\n")]
    total_tokens, total_prices = 0, 0
    total_tokens_pt2, total_prices_pt2 = 0, 0

    for dx1, dy1, dx2, dy2, x, y in lines:

        # part 1
        # result = min_tokens_needed(dx1, dy1, dx2, dy2, x, y) #same result!
        result = min_tokens_z3(dx1, dy1, dx2, dy2, x, y, max_pushes=100)
        if result is not None:
            total_tokens += result[0]
            total_prices += 1

        # part 2
        result = min_tokens_z3(dx1, dy1, dx2, dy2, x, y, add=10000000000000)
        if result is not None:
            total_tokens_pt2 += result[0]
            total_prices_pt2 += 1

    print("Part 1, minimal", total_tokens, "tokens for", total_prices, "prices")
    print("Part 2, minimal", total_tokens_pt2, "tokens for", total_prices_pt2, "prices")
