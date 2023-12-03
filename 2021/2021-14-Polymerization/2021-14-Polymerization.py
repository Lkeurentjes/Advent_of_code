from collections import Counter

with open('2021-14-Polymerization.txt') as f:
    lines = f.read().splitlines()

template = lines[0]

adddict = {}
for l in lines[2:]:
    l = l.split(" -> ")
    adddict[l[0]] = (l[0][0]+l[1], l[1]+l[0][1])

key_count = dict.fromkeys(adddict.keys(),0)
char_count = Counter()
char_count.update(template)

#start
for i in range(1,len(template)):
    key_count[template[i-1:i+1]] +=1

steps = 40
def count(steps, key_counter,char_count):
    char_counter = char_count.copy()
    for s in range(steps):
        newdict = dict.fromkeys(key_counter.keys(),0)
        for key, value in key_counter.items():
            if value != 0:
                newdict[adddict[key][0]] += value
                newdict[adddict[key][1]] += value
                char_counter.update({adddict[key][1][0]:value} )
        key_counter = newdict
    return max(char_counter.values())- min((char_counter.values()))

print("Part 1, the answer is", count(10, key_count, char_count))
print("Part 2, the answer is", count(40, key_count, char_count))

