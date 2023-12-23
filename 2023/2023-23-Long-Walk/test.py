import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math

with open('2023-23-Long-Walk.txt') as f:
    lines = f.read().splitlines()
# D = open(sys.argv[1]).read().strip()
# L = D.split('\n')
grid = [[c for c in row] for row in lines]
height = len(grid)
Width = len(grid[0])

sys.setrecursionlimit(10 ** 6)


def solve(part1):
    visited = set()
    for r in range(height):
        for c in range(Width):
            nbr = 0
            for dr, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= r + dr < height and 0 <= c + dc < Width and grid[r + dr][c + dc] != '#'):
                    nbr += 1
            if nbr > 2 and grid[r][c] != '#':
                visited.add((r, c))

    for c in range(Width):
        if grid[0][c] == '.':
            visited.add((0, c))
            start = (0, c)
        if grid[height - 1][c] == '.':
            visited.add((height - 1, c))
            end = (height - 1, c)

    E = {}
    for (rv, cv) in visited:
        E[(rv, cv)] = []
        Q = deque([(rv, cv, 0)])
        SEEN = set()
        while Q:
            r, c, d = Q.popleft()
            if (r, c) in SEEN:
                continue
            SEEN.add((r, c))
            if (r, c) in visited and (r, c) != (rv, cv):
                E[(rv, cv)].append(((r, c), d))
                continue
            for ch, dr, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= r + dr < height and 0 <= c + dc < Width and grid[r + dr][c + dc] != '#'):
                    if part1 and grid[r][c] in ['<', '>', '^', 'v'] and grid[r][c] != ch:
                        continue
                    Q.append((r + dr, c + dc, d + 1))

    count = 0
    ans = 0
    SEEN = [[False for _ in range(Width)] for _ in range(height)]
    seen = set()

    def dfs(v, d):
        nonlocal count
        nonlocal ans
        count += 1
        r, c = v
        if SEEN[r][c]:
            return
        SEEN[r][c] = True
        if r == height - 1:
            ans = max(ans, d)
        for (y, yd) in E[v]:
            dfs(y, d + yd)
        SEEN[r][c] = False

    dfs(start, 0)
    # print(count)
    return ans


print(solve(True))
print(solve(False))
