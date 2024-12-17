import re

def execute_program(registers, program):
    A, B, C = registers

    # Instruction pointer starts at 0
    ip = 0
    output = []


    # Execute program
    while ip < len(program):
        combo_val = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}
        opcode = program[ip]  # Fetch opcode
        operand = program[ip + 1]  # Fetch operand

        match opcode:
            case 0:  # adv: Division -> Store in A
                denominator = 2 ** combo_val[operand]
                A = A // denominator
            case 1:  # bxl: B XOR literal operand -> B
                B = B ^ operand
            case 2:  # bst: Combo operand % 8 -> B
                B = combo_val[operand] % 8
            case 3:  # jnz: Jump if A != 0
                if A != 0:
                    ip = operand
                    continue  # Do not increment ip after jump
            case 4:  # bxc: B XOR C -> B
                B = B ^ C
            case 5:  # out: Output combo operand % 8
                output.append(combo_val[operand] % 8)
            case 6:  # bdv: Division -> Store in B
                denominator = 2 ** combo_val[operand]
                B = A // denominator
            case 7:  # cdv: Division -> Store in C
                denominator = 2 ** combo_val[operand]
                C = A // denominator


        # Move instruction pointer to the next instruction
        ip += 2

    return output


def find_register_a_for_self_output(registers, program):
    numbers = []
    todo = [(len(program) - 1, 0)]  # Start from the last position of the program with value '0'
    for p, v in todo:
        # Test all possible values of 'a' within the range [8*v, 8*(v+1) - 1] --> 2^3 = 8 (cause 3 bits computer)
        for a in range(8 * v, 8 * (v + 1)):
            # Check if running the program with the current 'a' produces the remaining part of the program
            if execute_program([a, registers[1], registers[2]], program) == program[p:]:
                if p == 0:  # If we're at the start of the program, we've found a valid 'a'
                    numbers.append(a)
                else:
                    # Otherwise, move one step back and continue searching for valid 'a' values
                    todo += [(p - 1, a)]
    # Return the smallest valid 'a' that satisfies the condition
    return min(numbers)


with open('2024-17-Chronospatial_Computer.txt') as f:
    registers, program = f.read().split("\n\n")
    registers = list(map(int, re.findall(r'\d+', registers)))
    program = list(map(int, re.findall(r'\d+', program)))

    # # Run the program
    result = execute_program(registers, program)
    print("Part 1, The Output is", ','.join(map(str, result)))

    result_a = find_register_a_for_self_output(registers, program)
    print("Part 2, Lowest A value for the output is", result_a)
