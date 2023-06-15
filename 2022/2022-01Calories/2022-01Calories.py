with open("2022-01Calories.txt") as f:
    lines = f.read().splitlines()

mostcalories = 0
elfcalorie = 0
i =1

calorielist = []

calorie = 0
for l in lines:
    if l == "":
        #part 1
        if calorie > mostcalories:
            mostcalories = calorie
            elfcalorie = i
        i+=1

        # part 2
        calorielist.append(calorie)

        calorie = 0
        continue
    calorie += int(l)
calorielist.sort(reverse=True)


print("PART 1: elf",elfcalorie,"caries", mostcalories)
print("PART 2: The top three 11 carry :",calorielist[0]+calorielist[1]+calorielist[2], "calories")