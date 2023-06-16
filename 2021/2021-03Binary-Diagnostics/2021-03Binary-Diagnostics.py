with open('2021-03Binary-Diagnostics.txt') as f:
    lines = f.read().splitlines()

gamma_rate_bi = ""
epsilon_rate_bi = ""
oxygen_rate_bi = ""
co2_rate_bi = ""

for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for j in range(len(lines)):
        if lines[j][i] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma_rate_bi += "0"
        epsilon_rate_bi += "1"
    else:
        gamma_rate_bi += "1"
        epsilon_rate_bi += "0"

gamma_rate = int(gamma_rate_bi,2)
epsilon_rate = int(epsilon_rate_bi,2)

powerconsumption = gamma_rate * epsilon_rate
print("PART 1: gamma rate =",gamma_rate," and epsilon_rate =", epsilon_rate, "so the powerconsumption  =", powerconsumption  )

def get_binary(lines, position, kind):
    ones = []
    zeros = []

    for line in lines:
        if line[position] == "1":
            ones.append(line)
        else:
            zeros.append(line)

    if kind == "ox":
        if len(ones) >= len(zeros):
            new_lines = ones
        else:
            new_lines = zeros
    else:
        if len(ones) < len(zeros):
            new_lines = ones
        else:
            new_lines = zeros

    if len(new_lines) == 1:
        return new_lines[0]
    return get_binary(new_lines, position+1, kind)

oxygen_rate_bi = get_binary(lines, 0, "ox")
co2_rate_bi = get_binary(lines, 0, "co2")

oxygen_rate =  int(oxygen_rate_bi,2)
co2_rate = int(co2_rate_bi,2)
lifesupport = oxygen_rate * co2_rate
print("PART 2: oxygen rate =",oxygen_rate," and co2_rate =", co2_rate, "so the life support  =", lifesupport  )
