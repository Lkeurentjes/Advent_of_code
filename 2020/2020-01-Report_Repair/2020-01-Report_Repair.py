def sum_multiply(numbers, target):
    numbers_set = set(numbers)
    for n in numbers_set:
        if (target - n) in numbers_set:
            return n * (target - n)
    return 0

def sum_multiply_3(numbers, target):
    numbers_set = set(numbers)
    for i, n1 in enumerate(numbers):
        for n2 in numbers[i+1::]:
            if (target - n1 - n2) in numbers_set:
                return n1 * n2 * (target - n1- n2)
    return 0

with open('2020-01-Report_Repair.txt') as f:
    lines = [int(f) for f in f.read().splitlines()]
    print("Part 1, multiplication is", sum_multiply(lines, 2020))
    print("Part 2, multiplication is", sum_multiply_3(lines, 2020))
