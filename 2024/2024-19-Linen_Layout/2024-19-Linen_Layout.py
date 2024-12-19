from functools import lru_cache

def count_possible_designs(towel_patterns, designs):

    def can_construct_design(design):
        # list of boolean where 0, is true (cause empty space exist) and the false per stripe
        stripe_bool = [True] + [False] * (len(design))

        for i in range(1, len(design) + 1):
            for j in range(i):
                # check if design exists AND if character before was in existing pattern
                if design[j:i] in towel_patterns and stripe_bool[j]:
                    stripe_bool[i] = True
                    break

        return stripe_bool[len(design)]

    # Count the number of possible designs
    return sum(can_construct_design(design) for design in designs)

def count_arrangements(towel_patterns, designs):

    @lru_cache # use lru cashe to cashe results, so that know sub designs are only counted once
    def ways_to_construct(design):
        # return 1 is part = "" (which is the end)
        if not design:
            return 1

        count = 0
        # Try every part of the design
        for i in range(1, len(design) + 1):
            part = design[:i]
            if part in towel_patterns:
                # If the part is in the towel set, count ways to construct the remaining suffix
                count += ways_to_construct(design[i:])
        return count

    # Calculate total number of ways for all designs
    return sum(ways_to_construct(design) for design in designs)


with open('2024-19-Linen_Layout.txt') as f:
    patterns, designs = f.read().split("\n\n")
    patterns = set(patterns.split(", "))
    designs = designs.split("\n")
    
    print("Part 1, possible patterns are",count_possible_designs(patterns, designs))
    print("Part 2, sum of possible arrangements are",count_arrangements(patterns, designs))
