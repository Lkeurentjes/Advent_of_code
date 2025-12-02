def Dial(lines, start=50, zero=0, end=99, count_mid_rotation=False):
    Position = start
    MaxEnd = end + 1
    Count = 0
    
    for line in lines:
        letter = line[0]
        number = int(line[1:])
        if count_mid_rotation:
            if letter == "L":
                Count += (Position // MaxEnd) - ((Position - number) // MaxEnd)
            if letter == "R":
                Count += ((Position + number) // MaxEnd) - (Position // MaxEnd)

        if letter == "L":
            Position = (Position - number) % MaxEnd
        if letter == "R":
            Position = (Position + number) % MaxEnd

        if Position == zero and not count_mid_rotation:
            Count += 1

    return Count


with open('2025-01-SecretEntrence.txt') as f:
    lines = f.read().splitlines()
    print("Part 1, count of zeros is:",Dial(lines))
    print("Part 2, count of zeros is:",Dial(lines, count_mid_rotation=True))
