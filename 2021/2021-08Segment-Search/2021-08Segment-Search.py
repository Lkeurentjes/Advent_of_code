segmentdict = {}
segmentdictcount = {2:1, 3:7, 4:4, 7:8}


def count1478(segments):
    count = 0
    for seg in segments:
        if len(seg) in segmentdictcount.keys():
            count+=1
    return count

def decoder(input, output):
    input_sorted = sorted(input, key=len)
    for i in range(len(input_sorted)):
        input_sorted[i] = ''.join(sorted(input_sorted[i]))
    decoderdict = {}
    decoderdict[1] = input_sorted[0]
    decoderdict[4] = input_sorted[2]
    decoderdict[7] = input_sorted[1]
    decoderdict[8] = input_sorted[9]
    partof4_needed = decoderdict[4].replace(decoderdict[1][0], '').replace(decoderdict[1][1], '')


    input5 = input_sorted[3:6]
    for i5 in input5:
        if decoderdict[1][0] in i5 and decoderdict[1][1] in i5 :
            decoderdict[3] = i5
        elif partof4_needed[0] in i5 and partof4_needed[1] in i5:
            decoderdict[5] = i5
        else:
            decoderdict[2] = i5


    input6 = input_sorted[6:9]
    for i6 in input6:
        if partof4_needed[0] in i6 and partof4_needed[1] in i6:
            if decoderdict[1][0] in i6 and decoderdict[1][1] in i6:
                decoderdict[9] = i6
            else:
                decoderdict[6] = i6
        else:
            decoderdict[0] = i6

    # print(decoderdict)
    coderdict = {v: str(k) for k, v in decoderdict.items()}
    # print(coderdict)
    number = ""
    for i in output:
        number += (coderdict[''.join(sorted(i))])

    return int(number)



with open('2021-08Segment-Search.txt') as f:
    lines = f.read().splitlines()

count = 0
sum_decoded = 0
for line in lines:
    input_values = line.split(" | ")[0].split()
    output_values = line.split(" | ")[1].split()
    count += count1478(output_values)
    sum_decoded += decoder(input_values, output_values)

print("Part 1: the total count of output values is: ",count)
print("Part 2: the sum of the output values is: ",sum_decoded)