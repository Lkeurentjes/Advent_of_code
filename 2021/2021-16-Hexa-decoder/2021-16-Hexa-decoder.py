import numpy as np

global SUM_VERSION

def product(list):
    p = 1
    for i in list:
        p*=i
    # print("product",list, p)
    return p

def hex_to_4bitBin(hex):
    hex_integer = int(hex, 16)
    bin = '{0:04b}'.format(hex_integer)
    return bin


def get_len_subpackets(bin, number):
    index = 0
    n = 0
    while index < len(bin):
        if n == number:
            return index

        if len(set(bin[index::])) == 1:
            break

        type = int(bin[index + 3:index + 6], 2)
        index += 6

        if type == 4:
            while bin[index] != "0":
                index += 5
            index += 5
            n += 1
        else:
            # operator
            n += 1
            if bin[index] == "0":
                length = int(bin[index + 1: index + 16], 2)
                index += 1 + 15
                index += length

            else:
                nbr = int(bin[index + 1: index + 12], 2)
                index += 1 + 11
                index += get_len_subpackets(bin[index:], nbr)

    return index


def get_values(bin, i = 1):
    global SUM_VERSION
    index = 0
    values = []
    while index < len(bin):

        if len(set(bin[index::])) == 1:
            break

        version = int(bin[index:index + 3], 2)
        type = int(bin[index + 3:index + 6], 2)

        SUM_VERSION += version


        index += 6
        if type == 4:
            bin_number = ""
            while bin[index] != "0":
                bin_number += bin[index + 1:index + 5]
                index += 5
            bin_number += bin[index + 1:index + 5]
            index += 5
            values.append(int(bin_number, 2))

        else:
            # operator
            if bin[index] == "0":
                length = int(bin[index + 1: index + 16], 2)
                index += 1 + 15

            else:
                number = int(bin[index + 1: index + 12], 2)
                index += 1 + 11
                length = get_len_subpackets(bin[index:], number)


            val = get_values(bin[index:index + length], i+1)
            index += length

            if type == 0:
                values.append(sum(val))
            elif type == 1:
                values.append(product(val))
            elif type == 2:
                values.append(min(val))
            elif type == 3:
                values.append(max(val))
            elif type == 5:
                v = 1 if val[0] > val[1] else 0
                values.append(v)
            elif type == 6:
                v = 1 if val[0] < val[1] else 0
                values.append(v)
            elif type == 7:
                v = 1 if val[0] == val[1] else 0
                values.append(v)

    return values


with open('2021-16-Hexa-decoder.txt') as f:
    lines = f.read()
bin = ''.join(hex_to_4bitBin(c) for c in lines)
SUM_VERSION = 0


value = get_values(bin)
print("Part 1, sum of the versions is", SUM_VERSION)
print("Part 2 has a value of", value[0])
