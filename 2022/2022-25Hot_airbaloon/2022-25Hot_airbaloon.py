import math

def SNAFU_to_decimal(SNAFU):
    SNAFU_dict = {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}
    decimal = 0
    for i, char in enumerate(SNAFU[::-1]):
        # print(i, char, (5**i) * SNAFU_dict[char])
        decimal += (5 ** i) * SNAFU_dict[char]
    # print(SNAFU, decimal)
    return decimal


def decimal_to_SNAFU(decimal):
    SNAFUback_dict = {1: "1", 2: "2", 0: "0", -1: "-", -2: "="}
    SNAFU = ""

    div = 1
    while decimal >= div:
        div*=5
    div /= 5

    while True:
        if div == 1:
            lastnum = decimal
            if lastnum <= 2:
                SNAFU += SNAFUback_dict[lastnum]

            elif lastnum <= 5:
                smallernum = 1
                remaninder = lastnum - 5
                SNAFU += (SNAFUback_dict[smallernum] + SNAFUback_dict[remaninder])

            elif lastnum <= 10:
                smallernum = 1
                remaninder = lastnum - 5
                SNAFU += (SNAFUback_dict[smallernum] + SNAFUback_dict[remaninder])
            return SNAFU

        lastnum = decimal // div
        print( div, lastnum)

        if lastnum == 0:
            pass

        elif lastnum <= 2:
            SNAFU += SNAFUback_dict[lastnum]

        elif lastnum <= 5:
            smallernum = 1
            remaninder = lastnum - 5
            SNAFU += (SNAFUback_dict[smallernum] + SNAFUback_dict[remaninder])

        elif lastnum <= 10:
            smallernum = 2
            remaninder = lastnum - 5
            SNAFU += (SNAFUback_dict[smallernum] + SNAFUback_dict[remaninder])


        # print("SNAFU", SNAFU)
        # print("Lastnum", lastnum)

        decimal -= (lastnum*div)
        div //= 5

    # return SNAFU



with open('2022-25Hot_airbaloon.txt') as f:
    lines = f.read().splitlines()

    tank = 0
    for line in lines:
        tank += SNAFU_to_decimal(line)
    print(tank)
    # part_1 = decimal_to_SNAFU(tank)
    part_1 = decimal_to_SNAFU(40)
    print( "Translation is:", part_1, "translating back works", SNAFU_to_decimal(part_1))

