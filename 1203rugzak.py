with open("1203rugzak.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    productsum = 0
    # for line in lines:
    #
    #     same= set(line[:len(line) // 2]).intersection(set(line[len(line)//2:]))
    #     l = lambda x: ord(x) - 96 if x.islower() else ord(x) - 64 + 26
    #     productsum +=l(list(same)[0])
    for i in range(len(lines)//3):
        same = set(lines[0+i*3]).intersection(set(lines[1+i*3])).intersection(set(lines[2+i*3]))
        l = lambda x: ord(x) - 96 if x.islower() else ord(x) - 64 + 26
        productsum +=l(list(same)[0])

print(productsum)