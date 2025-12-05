import numpy as np

def checkRanges(ranges, ids):
    # Convert ranges to arrays
    start = np.array([r[0] for r in ranges])
    end = np.array([r[1] for r in ranges])
    ids = np.array(ids)
    # Check freshness using mask and its sum
    mask = ((ids[:, None] >= start) & (ids[:, None] <= end)).any(axis=1)
    count = mask.sum()
    return count

def countunique(ranges):
    ranges.sort(key=lambda x: x[0])

    uniquecount = 0
    start,end = ranges[0]
    for startnew, endnew in ranges[1:]:
        #if possible combine range
        if startnew <= end +1:
            if endnew > end:
                end = endnew
        # otherwise count range and go to the next
        else:
            uniquecount += (end - start) + 1
            start = startnew
            end = endnew

    # last interval
    uniquecount += (end - start + 1)

    return uniquecount

with open('2025-05-Cafetaria.txt') as f:
    parts = f.read().split("\n\n")  # Split into two sections
    ranges = [tuple(map(int, line.split("-"))) for line in parts[0].splitlines()]
    ids = [int(line) for line in parts[1].splitlines()]
    print("part 1, fresh ingriedients are:", checkRanges(ranges, ids))
    print("part 2, unique fresh ingriedients are:", countunique(ranges))
