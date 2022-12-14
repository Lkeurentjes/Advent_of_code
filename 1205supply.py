with open("1205suply.txt") as f:
    lines = f.read().splitlines()
    # print(lines)
    numberStacks = 0
    moves = []
    for i in range(len(lines)):
        if lines[i] == "":
            numberStacks = i-1
        elif lines[i][0] == "m":
            move=lines[i].split(" ")
            moves.append((int(move[1]),(int(move[3]),int(move[5]))))

    numberOfStacks = int(sorted(lines[numberStacks],reverse=True)[0])
    stackdict = {}
    for i in range(numberOfStacks):
        stackdict[i+1] = []
    # print(numberOfStacks)
    for i in range(numberStacks-1,-1,-1):
        for j in range(numberOfStacks):
            # print(lines[i][1 + j * 4])
            try:
                letter = lines[i][1+j*4]
                # print(letter)
            except:
                break
            else:
                if letter == " ":
                    continue
                stackdict[j+1].append(letter)
    print(stackdict)
    # print(moves)
    for move in moves:

        # for i in range(1,move[0]+1):
        #     stackdict[move[1][1]] = stackdict[move[1][1]] + (stackdict[move[1][0]][-1:])
        #     stackdict[move[1][0]] = stackdict[move[1][0]][:-1]
        # print(move, stackdict)

        #part 2
        stackdict[move[1][1]] = stackdict[move[1][1]] + (stackdict[move[1][0]][-(move[0]):])
        stackdict[move[1][0]] = stackdict[move[1][0]][:-(move[0])]

    print(stackdict)
    string = ""
    for list in stackdict.values():
        string+=list[-1]
    print(string)




