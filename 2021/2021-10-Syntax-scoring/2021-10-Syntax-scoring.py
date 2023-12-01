def recursive_check(error):
    replace = False
    if error.find("()") != -1:
        replace = True
        error = error.replace("()", "")
    if error.find("{}") != -1:
        replace = True
        error = error.replace("{}", "")
    if error.find("[]") != -1:
        replace = True
        error = error.replace("[]", "")
    if error.find("<>") != -1:
        replace = True
        error = error.replace("<>", "")
    # print(error)
    if replace:
        return recursive_check(error)
    else:
        return error


with open('2021-10-Syntax-scoring.txt') as f:
    lines = f.read().splitlines()
    print(lines)

# pointdict = {")": 3,
#              "]": 57,
#              "}": 1197,
#              ">": 25137}
pointdict = {0: 3,
              1: 57,
              2: 1197,
              3: 25137}

pointdict2 = {"(": 1,
             "[": 2,
             "{": 3,
             "<": 4}

score = 0
score2 = []
for l in lines:
    rest = recursive_check(l)
    a = rest.find(")")
    b = rest.find("]")
    c = rest.find("}")
    d = rest.find(">")
    if (a + b + c + d) != -4:
        test = [a, b, c, d]
        least = [t for t in test if t > 0]
        index = test.index(min(least))
        score += pointdict[index]
    else:
        scoreline = 0
        for c in rest[::-1]:
            scoreline = scoreline* 5 + pointdict2[c]
        score2.append(scoreline)

score2.sort()


print("Answer of part 1 is: ", score)
print("Answer of part 2 is: ", score2[int(len(score2)/2 -0.5)])