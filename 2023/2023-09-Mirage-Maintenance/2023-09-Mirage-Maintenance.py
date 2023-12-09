def sequincemaker(seq):
    new_seq = [s - seq[i] for i, s in enumerate(seq[1::])]
    test = all(s == 0 for s in new_seq)
    if test:
        return seq
    else:
        subseq = sequincemaker(new_seq)
        seq.append(seq[-1]+subseq[-1])
        seq.insert(0, seq[0]-subseq[0])
        return seq

with open('2023-09-Mirage-Maintenance.txt') as f:
    lines = f.read().splitlines()
    lines = [[int(x) for x in line.split()] for line in lines]

sum = 0
sumfirst =0
for line in lines:
    seq = sequincemaker(line)
    sum += seq[-1]
    sumfirst += seq[0]

print("part 1, has a sum of", sum)
print("part 2, has a sum of", sumfirst)