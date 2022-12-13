import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "1210test.txt")


def arrayRotate(arr, reverse):
    if reverse:
        arr[:] = arr[1:] + arr[0:1]
    else:
        arr[:] = arr[-1:] + arr[0:-1]
    return arr


with open(INPUT_FILE, "r", encoding="UTF-8") as str_file:
    instructions = str_file.read().splitlines()

    signalStrengths = []
    cycles = 0
    x = 1

    sprite = "###....................................."
    # sprite = "###                                     "
    sprite = [pixel for pixel in sprite]
    currentRow = []
    display = []


    def extractInfo(instruction):
        cyclesToComplete = 0
        addX = 0

        if 'noop' in instruction:
            cyclesToComplete = 1
        else:
            cyclesToComplete = 2
            addX = int(instruction.split(' ')[1])

        return [cyclesToComplete, addX]


    for instruction in instructions:
        [cyclesToComplete, addX] = extractInfo(instruction)

        for i in range(0, cyclesToComplete):
            cycles += 1

            if ((cycles - 20) % 40 == 0):
                signalStrengths.append(x * cycles)

            if len(currentRow) == 40:
                display.append(currentRow)
                currentRow = []

            currentRow.append(sprite[(cycles - 1) % 40])

        if addX != 0:
            x += addX

            for i in range(0, abs(addX)):
                if addX > 0:
                    sprite = arrayRotate(sprite, False)
                else:
                    sprite = arrayRotate(sprite, True)

    # part 1
    print(sum(signalStrengths))

    # part 2
    display.append(currentRow)

    for row in display:
        print("".join(row))