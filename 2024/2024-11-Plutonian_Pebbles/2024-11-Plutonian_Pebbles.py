from collections import Counter

def process_stone_changes(stone_counts):
    """Process stone changes for a single blink."""
    new_counts = Counter()

    for stone, count in stone_counts.items():
        if stone == 0:
            # Replace all 0 stones with stones marked 1
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            # Split stones with even-digit numbers into two stones
            stone_str = str(stone)
            mid = len(stone_str) // 2
            new_counts[int(stone_str[:mid])] += count
            new_counts[int(stone_str[mid:])] += count
        else:
            # Multiply stones with odd-digit numbers by 2024
            new_stone = stone * 2024
            new_counts[new_stone] += count

    return new_counts

def simulate_blinks(start_stones, num_blinks):
    """Simulate the blinking process for a given number of blinks."""
    stone_counts = Counter(start_stones)

    for _ in range(num_blinks):
        stone_counts = process_stone_changes(stone_counts)

    return stone_counts

if __name__ == "__main__":
    with open('2024-11-Plutonian_Pebbles.txt') as file:
        start_stones = [int(x) for x in file.read().split()]

    # Part 1: After 25 blinks
    stone_counts = simulate_blinks(start_stones, 25)
    print("Part 1: number of stones after 25 blinks:", sum(stone_counts.values()))

    # Part 2: After 75 blinks
    stone_counts = simulate_blinks(start_stones, 75)
    print("Part 2: number of stones after 75 blinks:", sum(stone_counts.values()))
