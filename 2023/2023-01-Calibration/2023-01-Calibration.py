with open('2023-01-Calibration.txt') as f:
    lines = f.read().splitlines()
    print(lines)

sum = 0
for l in lines:
    digits = [str(i) for i in l if i.isdigit()]
    sum += int(digits[0] + digits[-1])

print("Answer to part 1 is: ", sum)

numintdict = {"one" :1,"two" :2,"three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
sum2 = 0
for l in lines:
    digits=[]

    # get first
    for i in range(0,len(l)-1):
        found = False
        if  l[i].isdigit():
            digits.append(str(l[i]))
            break
        else:
            for key in numintdict.keys():
                index = l[i:].find(key)
                if index == 0:
                    digits.append(str(numintdict[key]))
                    found=True
                    break
            if found:
                break
    # get last
    for i in range(len(l)-1,0,-1):
        found = False
        if  l[i].isdigit():
            digits.append(str(l[i]))
            break
        else:
            for key in numintdict.keys():
                index = l[i:].find(key)
                if index == 0:
                    digits.append(str(numintdict[key]))
                    found=True
                    break
            if found:
                break
    sum2 += int(digits[0] + digits[-1])

print("Answer to part 2 is: ", sum2)





