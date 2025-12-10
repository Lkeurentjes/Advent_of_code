from collections import deque
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def switch(now, button):
    return tuple([(v ^ 1) if i in button else v for i, v in enumerate(now)])

def min_on_click_bfs(now, indicator, buttons):
    # unlikely but test
    if now == indicator:
        return 0, []

    #Queue
    q = deque([(now, [])])
    visited = {now}

    #BFS
    while q:
        state, b_used = q.popleft()

        # Press all the buttons
        for b_idx, button in enumerate(buttons):
            nxt = switch(state, button)
            if nxt in visited:
                continue
            b_now_used = b_used + [b_idx]
            if nxt == indicator:
                return len(b_now_used), b_now_used
            visited.add(nxt)
            q.append((nxt, b_now_used))

    return None, None

def build_matrix(buttons, Joltage):
    n = len(Joltage)
    m = len(buttons)
    A = np.zeros((n, m), dtype=int)
    for j, indices in enumerate(buttons):
        for i in indices:
            A[i, j] = 1
    return A


def min_presses(buttons, Joltage):
    A = build_matrix(buttons, Joltage)
    b = np.array(Joltage)
    m = A.shape[1]

    c = np.ones(m)  # minimaliseer som(x)
    integrality = np.ones(m, dtype=int)
    bounds = Bounds(np.zeros(m), np.full(m, np.inf))
    constraints = [LinearConstraint(A, b, b)]

    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)

    if res.success:
        x = res.x.astype(int)
        total = int(res.fun)
        # print("Minimum total presses:", total)
        # print("Counts per button:", x.tolist())
        return total, x.tolist()
    else:
        # print("No optimal solution found.")
        return None, None

def fix_the_machines(machines, part1 = True):
    mincount = 0
    for indicator,buttons,joltage in machines:
        now = tuple([0 for x in range(len(indicator))])
        # print(now, indicator,buttons,joltage)
        if part1:
            count, buttonsclicked = min_on_click_bfs(now, indicator, buttons)
            mincount += count
            # print(count, buttonsclicked)
        else:
            count, buttonsclicked = min_presses(buttons, joltage)
            mincount += count
            # print(count, buttons)
    return mincount



with open('2025-10-Factory.txt') as f:
    lines = f.read().splitlines()
    machines = []
    for line in lines:
        line = line.split()
        indicator = tuple([1 if ch == '#' else 0 for ch in line[0].replace("[","").replace("]","")])
        buttons = [list(map(int, s[1:-1].split(','))) for s in line[1:-1]]
        joltage = tuple([int(l) for l in line[-1].replace("{","").replace("}","").split(",")])
        machines.append((indicator,buttons,joltage))
    print("part 1, mincount for all machines is", fix_the_machines(machines))
    print("part 2, mincount for all machines is", fix_the_machines(machines, False))

