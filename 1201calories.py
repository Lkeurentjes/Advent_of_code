with open("1201calories.txt") as f:
    lines = f.read().splitlines()
    # print(lines)
    mostcalories = 0
    calorielist = []
    elfcalorie = 0
    i =1
    calorie = 0
    for l in lines:
        if l == "":
            # if calorie > mostcalories:
            #     mostcalories = calorie
            #     elfcalorie = i
            # i+=1
            calorielist.append(calorie)
            calorie = 0
            continue
        calorie += int(l)
    calorielist.sort(reverse=True)
    print(calorielist)
    print(calorielist[0]+calorielist[1]+calorielist[2])
    print(elfcalorie, mostcalories)
