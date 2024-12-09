def recursive_finder(code, low, high):
    if len(code) == 1:
        if code in "FL":
            return low
        else:
            return high

    half = (high - low) // 2
    if code[0] in "FL":
        return recursive_finder(code[1:], low, low + half)
    else:
        return recursive_finder(code[1:], low + half + 1, high)

def find_seat(ids):
    sorted_ids = sorted(ids)

    for i in range(len(sorted_ids) - 1):
        if sorted_ids[i + 1] - sorted_ids[i] == 2:
            return sorted_ids[i] + 1
    return -1

with open('2020-05-Binary_Boarding.txt') as f:
    lines = f.read().splitlines()
    all_ids = []
    for card in lines:
        row = recursive_finder(card[0:7], 0, 127)
        chair = recursive_finder(card[7:], 0, 7)
        all_ids.append(row * 8 + chair)
    print("Part 1, max id of the boardingpasses is",max(all_ids))
    print("Part 2, my seat id is", find_seat(all_ids))

