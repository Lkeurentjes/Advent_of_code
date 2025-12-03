def HighestJoltage(banks):
    count = 0
    for bank in banks:
        maxJoltage = max(bank[:-1])
        maxindex = bank.index(maxJoltage)
        secondJoltage = max(bank[maxindex+1:])
        count += int(str(maxJoltage) + str(secondJoltage))
    return count

def HighestJoltage12(banks, Number=12):
    count = 0
    for bank in banks:
        numberstring = ""
        start = 0
        for remaining in range(Number, 0, -1):
            end = len(bank)-remaining+1
            maxJoltage = max(bank[start:end])
            start = bank.index(maxJoltage, start, end) + 1
            numberstring += str(maxJoltage)
        count += int(numberstring)
    return count


with open('2025-03-Lobby.txt') as f:
    lines = f.read().splitlines()
    banks = [ [int(n) for n in line] for line in lines]
    print("Part 1, sum of highest joltage",HighestJoltage(banks))
    print("Part 1, with part2 function", HighestJoltage12(banks, 2))
    print("Part 2, sum of highest joltage",HighestJoltage12(banks))
