from functools import lru_cache
import math

@lru_cache
def recursive_evaluator(result, current, numbers, part1=True):
    # check result
    if len(numbers) == 0:
        return result == current

    # early false
    if current > result:
        return False

    # Precompute digits for mathematical concatenation instead of int(str(current) + str(numbers[0]))
    digits = math.ceil(math.log10(numbers[0] + 1)) if numbers[0] > 0 and not part1 else 1

    return (recursive_evaluator(result, current + numbers[0], numbers[1:], part1) or  # summation
            recursive_evaluator(result, current * numbers[0], numbers[1:], part1) or  # multiplication
            (not part1 and recursive_evaluator(result, current * (10 ** digits) + numbers[0], numbers[1:], part1)))  # concatenation


with open('2024-07-Bridge_Repair.txt') as f:
    lines = f.read().splitlines()
    calibration = [(int(x.split(': ')[0]), tuple(map(int, x.split(': ')[1].split()))) for x in lines]

    total = 0
    for res, numbers in calibration:
        if recursive_evaluator(res, numbers[0], numbers[1:]):
            total += res
    print("part 1, evaluated result is", total)

    total = 0
    for res, numbers in calibration:
        if recursive_evaluator(res, numbers[0], numbers[1:], False):
            total += res
    print("part 2, evaluated result is", total)




