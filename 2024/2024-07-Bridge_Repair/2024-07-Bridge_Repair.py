def do_math_sum(result, currentSum, numbers, part1=True):
    # check sum this step
    if len(numbers) == 0:
        return result == currentSum

    else:
        currentSum += numbers[0]

        # early return
        if currentSum > result:
            return False

        # test all possible other math characters
        return (
                do_math_sum(result, currentSum, numbers[1:], part1) or
                do_math_multiply(result, currentSum, numbers[1:], part1) or
                (not part1 and
                 do_concatenation(result, currentSum, numbers[1:]))
        )


def do_math_multiply(result,multiplication,numbers, part1=True):
    if len(numbers) == 0:
        return multiplication == result

    else:
        multiplication *= numbers[0]

        # early return
        if multiplication > result:
            return False

        # test all possible other math characters
        return (
                do_math_sum(result,multiplication, numbers[1:], part1) or
                do_math_multiply(result, multiplication, numbers[1:], part1) or
                (not part1 and
                do_concatenation(result, multiplication, numbers[1:]))
        )

def do_concatenation(result, concatenation, numbers):
    if len(numbers) == 0:
        return concatenation == result
    else:
        concatenated_value = int(str(concatenation) + str(numbers[0]))

        #early return
        if concatenated_value > result:
            return False

        # test all possible other math characters
        return (
            do_math_sum(result, concatenated_value, numbers[1:], False) or
            do_math_multiply(result, concatenated_value, numbers[1:], False) or
            do_concatenation(result, concatenated_value, numbers[1:])
        )


with open('2024-07-Bridge_Repair.txt') as f:
    lines = f.read().splitlines()
    calibration = [(int(x.split(': ')[0]), list(map(int, x.split(': ')[1].split()))) for x in lines]
    total = 0
    for res, numbers in calibration:
        if do_math_sum(res,0, numbers) or do_math_multiply(res,1, numbers):
            total += res
    print("part 1, evaluated result is", total)

    total = 0
    for res, numbers in calibration:
        if do_math_sum(res, 0, numbers, False) or do_math_multiply(res, 1, numbers, False) or do_concatenation(res, 0, numbers):
            total += res
    print("part 2, evaluated result is", total)
