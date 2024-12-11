from collections import Counter

def blink_efficient(stone_counts):
    # make a new counter
    new_counts = Counter()

    # loop over the counter and change
    for stone, n in stone_counts.items():
        if stone == 0:
            # Replace all 0 by 1
            new_counts[1] += n
        elif len(str(stone)) % 2 == 0:
            # Split into two stones
            stone_str = str(stone)
            mid = len(stone_str) // 2
            new_counts[int(stone_str[:mid])] += n
            new_counts[int(stone_str[mid:])] += n
        else:
            # Multiply by 2024
            new_stone = stone * 2024
            new_counts[new_stone] += n

    return new_counts

def blinker(start, times):
    # order isn't important so use counter to make more efficient
    stone_counts = Counter(start)

    # blinking
    for _ in range(times):
        stone_counts = blink_efficient(stone_counts)

    return stone_counts


with open('2024-11-Plutonian_Pebbles.txt') as f:
    start_stones = [int(x) for x in f.read().split()]

    stone_counts = blinker(start_stones, 25)
    print("Part 1: number of stones after 25 blinks", sum(stone_counts.values()))

    stone_counts = blinker(start_stones, 75)
    print("Part 2: number of stones after 75 blinks", sum(stone_counts.values()))