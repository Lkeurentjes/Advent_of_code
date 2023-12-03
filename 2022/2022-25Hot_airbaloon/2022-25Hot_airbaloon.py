import math

def SNAFU_to_decimal(SNAFU):
    SNAFU_dict = {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}
    decimal = 0
    for i, char in enumerate(SNAFU[::-1]):
        decimal += (5 ** i) * SNAFU_dict[char]
    return decimal


def decimal_to_SNAFU(decimal):
    SNAFU = ""

    while decimal > 0:
        remainder = decimal % 5

        if remainder == 0:
            SNAFU = '0' + SNAFU
        elif remainder == 1:
            SNAFU = '1' + SNAFU
        elif remainder == 2:
            SNAFU = '2' + SNAFU
        else:
            remainder -= 5
            if remainder == -1:
                SNAFU = '-' + SNAFU
            elif remainder == -2:
                SNAFU = '=' + SNAFU
        decimal = (decimal - remainder) // 5

    return SNAFU



with open('2022-25Hot_airbaloon.txt') as f:
    lines = f.read().splitlines()

    tank = 0
    for line in lines:
        tank += SNAFU_to_decimal(line)
    part_1 = decimal_to_SNAFU(tank)

    print("Part 1 answer is in decimal", tank, " so in SNAFU it is", decimal_to_SNAFU(tank))


