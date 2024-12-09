import copy


def clean_up_disk(tupledisk):
    disk = copy.deepcopy(tupledisk)  # otherwise it changes thing for part 2
    compact_disk = [disk[0]]
    indexfree, indexlast = 1, len(disk) - 1

    # make the compact disk
    while indexfree <= indexlast:
        if disk[indexfree][1] == disk[indexlast][1]:
            # same size replace
            compact_disk.extend([disk[indexlast], disk[indexfree + 1]])
            indexfree += 2
            indexlast -= 2
        elif disk[indexfree][1] > disk[indexlast][1]:
            # put it here and change free size
            compact_disk.append(disk[indexlast])
            disk[indexfree] = (disk[indexfree][0], disk[indexfree][1] - disk[indexlast][1])
            indexlast -= 2
        else:
            # put partly here and keep in mind other part
            compact_disk.append((disk[indexlast][0], disk[indexfree][1]))
            disk[indexlast] = (disk[indexlast][0], disk[indexlast][1] - disk[indexfree][1])
            compact_disk.append(disk[indexfree + 1])
            indexfree += 2

    return compact_disk


def clean_up_disk_whole_files(tupledisk):
    set_used = set()

    for file_index in range(len(tupledisk) - 1, 0, -1):
        file = tupledisk[file_index]
        if file[0] != "free" and file not in set_used:
            set_used.add(file) # to make sure they can only be found ones

            # look for free space big enough
            for i, space in enumerate(tupledisk):
                if i >= file_index: # big enough space needs to be before
                    break

                if space[0] == "free":
                    if space[1] == file[1]:
                        # same space is change places
                        tupledisk[i], tupledisk[file_index] = tupledisk[file_index], tupledisk[i]
                        break
                    elif space[1] > file[1]:
                        # change part of free with disk
                        remaining = space[1] - file[1]
                        tupledisk[i], tupledisk[file_index] = file, ("free", file[1])
                        tupledisk.insert(i + 1, ("free", remaining))
                        break

    return tupledisk


def check_sum(compact_disk):
    checksum, position = 0, 0

    for block in compact_disk:
        file_id, length = block
        if file_id != "free":  # Only consider file blocks
            for _ in range(length):
                checksum += position * file_id
                position += 1
        else:  # Skip free space
            position += length

    return checksum


with open('2024-09-Disk_Fragmenter.txt') as f:
    lines = f.read()
    tuple_space = [(filenumber if i % 2 == 0 else "free", int(line))
                   for i, line in enumerate(lines)
                   for filenumber in [i // 2]]

    print("Part 1, Checksum of compact disk:", check_sum(clean_up_disk(tuple_space)))
    print("Part 2, Checksum of ordered disk:", check_sum(clean_up_disk_whole_files(tuple_space)))
