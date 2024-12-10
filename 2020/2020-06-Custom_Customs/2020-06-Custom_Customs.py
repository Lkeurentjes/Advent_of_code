def unique(group):
    groupset = set(group.replace("\n", ""))
    return len(groupset)

def all_same(group):
    grouplist = group.split("\n")

    same_set = set(grouplist[0])

    for group in grouplist[1:]:
        same_set = same_set & set(group)

    return len(same_set)

with open('2020-06-Custom_Customs.txt') as f:
    lines = f.read().split("\n\n")
    total = 0
    total_same = 0
    for group in lines:
        total += unique(group)
        total_same += all_same(group)
    print("Part 1, total yes is:", total)
    print("Part 2, total yes by all is:", total_same)
