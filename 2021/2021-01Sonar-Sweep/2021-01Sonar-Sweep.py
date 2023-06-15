with open('2021-01Sonar-Sweep.txt') as f:
    lines = f.read().splitlines()
    # print(lines)

number = int(lines[0])
counter = 0
for i in lines[1:]:
    i = int(i)
    if i > number:
        counter +=1
    number = i

print("PART 1: mesurment increased",counter,"times")

number = int(lines[0]) + int(lines[1]) + int(lines[2])
counter2 = 0
for i in range(1,len(lines)-2):
    sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if sum > number:
        counter2 +=1
    number = sum

print("PART 1: mesurments increased",counter2,"times")
