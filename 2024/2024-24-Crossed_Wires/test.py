#!/usr/bin/env pypy3

import sys

DEBUG = sys.argv.count('-v')


def parse_input():
    with open('2024-24-Crossed_Wires.txt') as f:
        lines = f.read().splitlines()
    # lines = [_.strip('\r\n') for _ in sys.stdin]
    inputs = {}
    gates = {}
    for line in lines:
        if ':' in line:
            inp, val = line.replace(':', '').split()
            inputs[inp] = int(val)
        elif '->' in line:
            w1, gate, w2, _, out = line.split()
            if w1[0] == 'y' and w2[0] == 'x':
                w1, w2 = w2, w1
            gates[out] = (gate, w1, w2)

    return (inputs, gates)


def part1(inputs, gates):
    # collect all wires and assign known value
    wires = {_: None for _ in gates}
    for inp, v in inputs.items():
        wires[inp] = v

    # while there are any unknowns, propagate ins to outs
    while any(_ is None for _ in wires.values()):
        for out, tup in gates.items():
            type, in1, in2 = tup
            if wires[out] is None:
                if wires[in1] is not None and wires[in2] is not None:
                    if type == 'AND':
                        wires[out] = (wires[in1] & wires[in2]) & 1
                    elif type == 'OR':
                        wires[out] = (wires[in1] | wires[in2]) & 1
                    elif type == 'XOR':
                        wires[out] = (wires[in1] ^ wires[in2]) & 1

    # compute output value, shift each bit into an int...
    x = 0
    for i in range(100):
        name = f'z{i:02d}'
        if name not in wires:
            break
        x |= (wires[name] << i)

    print(x)


def part2(inputs, gates):
    # Circuit just implements a full adder:
    #
    #   Zi = (Xi XOR Yi) XOR Ci-1
    #   Ci = (Xi AND Yi) OR ((Xi XOR Yi) AND Ci-1)
    #
    # Don't need to compute or simulate anything, just trace back structurally
    # from each Zi checking for bad outputs/inputs...

    bad = []

    zs = sorted([_ for _ in gates if _[0] == 'z'])
    Z0, ZN = zs[0], zs[-1]

    # Special case, Z0 = X0 XOR Y0
    type, in1, in2 = gates[Z0]
    if type != 'XOR':
        bad.append((Z0, f'{Z0} not XOR'))
    else:
        assert in1 == Z0.replace('z', 'x'), in1
        assert in2 == Z0.replace('z', 'y'), in2

    # Special case, ZN is just carry-out N-1
    type, in1, in2 = gates[ZN]
    if type != 'OR':
        bad.append((ZN, f'{ZN} not OR'))
    else:
        # just check they're and
        assert gates[in1][0] == 'AND'
        assert gates[in2][0] == 'AND'

    # otherwise, check each Zi
    for i in range(1, len(zs) - 1):
        c = f'c{i:02d}'
        x = f'x{i:02d}'
        y = f'y{i:02d}'
        z = f'z{i:02d}'

        # check output direct
        type, in1, in2 = gates[z]
        if type != 'XOR':
            bad.append((z, f'{z} not XOR {type}'))
            continue

        # inputs otherwise
        g1 = gates[in1]
        g2 = gates[in2]

        # make g1 Zi if it's Ci or g2 is Zi - either could be wrong...
        if g1[0] == 'OR' or g2[0] == 'XOR':
            in1, in2 = in2, in1
            g1, g2 = g2, g1

        if g1[0] != 'XOR':
            bad.append((in1, f'{z} in1 not XOR'))
        else:
            if g1[1] != x:
                bad.append((g1[1], f'{z} in1 XOR in1 not {x}'))
            if g1[2] != y:
                bad.append((g1[2], f'{z} in2 XOR in2 not {y}'))

        # check Ci
        if g2[0] == 'AND' and i == 1:
            # c0 is just X AND Y
            pass
        elif g2[0] != 'OR':
            bad.append((in2, f'{c} not OR'))
        else:
            in1p = gates[in2][1]
            g1p = gates[in1p]
            if g1p[0] != 'AND':
                bad.append((in1p, f'{c} in1 not AND {g1p[0]}'))

            in2p = gates[in2][2]
            g2p = gates[in2p]
            if g2p[0] != 'AND':
                bad.append((in2p, f'{c} in2 not AND {g2p[0]}'))

    if DEBUG:
        for item in bad:
            print(item)
        print(len(bad))

    b = sorted(set(_[0] for _ in bad))
    print(','.join(b))


def main():
    data = parse_input()

    if '1' in sys.argv:
        part1(*data)
    if '2' in sys.argv:
        part2(*data)
    part1(*data)
    part2(*data)


if __name__ == '__main__':
    main()