def checknumberrepeat(number):
    s = str(number)
    length = len(s)
    for k in range(1, length // 2 + 1):
        if length % k == 0:
            if s == s[:k] * (length // k):
                return number
    return 0


def checknumber(number):
    s = str(number)
    if len(s) % 2 == 0:  # only even length can be repeated twice
        half = len(s) // 2
        if s[:half] == s[half:]:
            return number
    return 0


def checkranges(ranges, part1=True):
    count = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if part1:
                count += checknumber(i)
            else:
                count += checknumberrepeat(i)
    return count


with open('2025-02-GiftShop.txt') as f:
    line = f.read().strip()
ranges = [(int(x), int(y)) for x, y in (r.split('-') for r in line.split(','))]

print("Part 1, sum of invalid id's is:", checkranges(ranges))
print("Part 2, sum of invalid id's is:", checkranges(ranges, part1=False))
