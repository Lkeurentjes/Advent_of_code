import copy

with open('2022-05Supplies.txt') as f:
    lines = f.read().splitlines()
    # print(lines)

numberStacks = 0
moves = []
for i in range(len(lines)):
    if lines[i] == "":
        numberStacks = i - 1
    elif lines[i][0] == "m":
        move = lines[i].split(" ")
        moves.append((int(move[1]), (int(move[3]), int(move[5]))))

numberOfStacks = int(sorted(lines[numberStacks], reverse=True)[0])
stackdict = {}
for i in range(numberOfStacks):
    stackdict[i + 1] = []

for i in range(numberStacks - 1, -1, -1):
    for j in range(numberOfStacks):
        try:
            letter = lines[i][1 + j * 4]
        except:
            break
        else:
            if letter == " ":
                continue
            stackdict[j + 1].append(letter)


stackdict2 = copy.deepcopy(stackdict)


for move in moves:

    for i in range(1, move[0] + 1):
        # part 1
        stackdict[move[1][1]] = stackdict[move[1][1]] + (stackdict[move[1][0]][-1:])
        stackdict[move[1][0]] = stackdict[move[1][0]][:-1]

    # part 2
    stackdict2[move[1][1]] = stackdict2[move[1][1]] + (stackdict2[move[1][0]][-(move[0]):])
    stackdict2[move[1][0]] = stackdict2[move[1][0]][:-(move[0])]


string1 = ""
for list in stackdict.values():
    string1 += list[-1]
print("PART 1: has crates", string1, "on top")

string2 = ""
for list in stackdict2.values():
    string2 += list[-1]
print("PART 2: has crates", string2, "on top")
