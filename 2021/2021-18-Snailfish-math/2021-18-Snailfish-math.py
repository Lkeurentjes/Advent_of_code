import ast
def explode(number):
    print("i need explode")
    print(number)
    return number

def split(number):
    print("i need a split")
    return number
def reduce(number, depth, addl = False, addr = False):
    if isinstance(number, int):
        if number > 10:
            return split(number)
    elif isinstance(number, list):
        if depth >= 4 and (isinstance(number[1], list)):
            return reduce(explode(number), depth, True, False)
        elif depth >=4 and (isinstance(number[0], list)):
            return reduce(explode(number), depth, False, True)
        else:
            return [reduce(number[0], depth+1), reduce(number[1], depth+1)]

    return number


def add(number, other):
    number = reduce([number, other],1)
    return number


with open('2021-18-Snailfish-math.txt') as f:
    lines = f.read().splitlines()

snailsum = ast.literal_eval(lines[0])
for l in lines[1:]:
    output_list = ast.literal_eval(l)
    snailsum = add(snailsum, output_list)

print(snailsum)