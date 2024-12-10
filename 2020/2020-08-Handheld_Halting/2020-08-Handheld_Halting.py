def boot_code(lines):
    acc = 0
    step = 0
    visited = set()
    while step < len(lines):

        # find loop
        if step in visited:
            return (acc, False)
        visited.add(step)

        if lines[step][0] == 'nop':
            step += 1
        elif lines[step][0] == 'acc':
            if lines[step][1] == "+": acc += int(lines[step][2])
            elif lines[step][1] == "-": acc -= int(lines[step][2])
            step += 1
        elif lines[step][0] == 'jmp':
            if lines[step][1] == "+": step += int(lines[step][2])
            elif lines[step][1] == "-": step -= int(lines[step][2])

    return (acc, True)

def fix_boot_code(lines):
    for i in range(len(lines)):
        OG_instruction = lines[i][0]
        # Only modify 'nop' or 'jmp'
        if OG_instruction == 'nop':
            lines[i][0] = 'jmp'
        elif OG_instruction == 'jmp':
            lines[i][0] = 'nop'
        else:
            continue

        # Test if the program terminates
        acc, terminates = boot_code(lines)
        if terminates:
            return acc  # Return the accumulator value if the program terminates

        # Restore the original instruction
        lines[i][0] = OG_instruction

    return None  # No modification fixed the program

with open('2020-08-Handheld_Halting.txt') as f:
    lines = [line.replace("-", "- ").replace("+", "+ ").split() for line in f.read().splitlines()]
    print("Part 1, acc after loop is", boot_code(lines)[0])
    print("Part 2, acc after fix is", fix_boot_code(lines))
