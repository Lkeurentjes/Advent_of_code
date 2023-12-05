def replace(seed, ranges):
    for new, old, length in ranges:
        if old <= seed < old + length:
            # print(seed, new, old, length)
            return new + seed - old
    return seed


def split_ranges(pair, ranges):  # will split ranges based on changes in ranges
    splits = []
    s, e = pair

    for new, old, length in ranges:
        if old <= s <= old + length and old <= e <= old + length:
            splits.append((new + s - old, new + e - old))
        elif old <= s <= old + length:
            end = old + length
            splits.append((new + s - old, new + end - old))
            s = end - 1
        elif old <= e <= old + length:
            start = old
            splits.append((new + start - old, new + e - old))
            e = start + 1
        elif s <= old <= e and s <= old + length <= e:
            splits.append((new, new + length))

    if not splits:
        return [pair]

    if pair != (s, e):
        splits.append((s, e))

    return splits


def apply_ranges(pairssl, allranges):
    pairs = [(s, s + l - 1) for s, l in pairssl]

    for ranges in allranges:
        newpairs = []
        for pair in pairs:
            newpairs += split_ranges(pair, ranges)
        pairs = newpairs

    pairs_sorted = sorted(pairs)

    return pairs_sorted[0][0]


with open('2023-05-Food-production-problem.txt') as f:
    lines = f.read().split("\n\n")

seeds = [int(seed) for seed in lines[0].split()[1::]]
seedspairs = list(zip(seeds[::2], seeds[1::2] + [None]))
allranges = [[[int(number) for number in r.split()] for r in l.split("\n")[1:]] for l in lines][1:]

for ranges in allranges:
    for i, s in enumerate(seeds):
        seeds[i] = replace(s, ranges)

print("Part 1 the minimum is", min(seeds))

seedsp2 = apply_ranges(seedspairs, allranges)

print("Part 2 the minimum is", seedsp2)
