from copy import deepcopy

import graphviz
from pathlib import Path

def evaluate_gate(a, b, gate_type):
    if gate_type == "AND":
        return a & b
    elif gate_type == "OR":
        return a | b
    elif gate_type == "XOR":
        return a ^ b
    else:
        raise ValueError(f"Unknown gate type: {gate_type}")

def simulate(wire_values, gates):
    while gates:
        remaining_gates = []

        for a, gate, b, out in gates:
            # Check if inputs are available
            try:
                # Evaluate the gate
                wire_values[out] = evaluate_gate(wire_values[a], wire_values[b], gate)
            except KeyError:
                # Inputs not yet available
                remaining_gates.append([a, gate, b, out])

        if len(remaining_gates) == len(gates):
            raise RuntimeError("Simulation stuck; possible invalid input or loop.")
        gates = remaining_gates

    return wire_values

def extract_output(wire_values, filter):
    wires = {wire: value for wire, value in wire_values.items() if wire.startswith(filter)}
    sorted_values = [value for key, value in sorted(wires.items(), reverse=True)]
    binary_string = "".join(str(bini) for bini in sorted_values)
    print(binary_string)
    return int(binary_string, 2)

def find_swaps(wire_values, gates):
    graph = graphviz.Digraph("2024day24Test")
    # manualPART
    swaps = [("ppk", "kpw"),("hgw", "tsp"),("djg", "grd"),("gbs", "cvf") ]
    new_gates = []
    for a, gate, b, out in gates:
        changes = False
        for swapA, swapB in swaps:
            if out == swapA:
                new_gates.append([a, gate, b, swapB])
                changes = True
                break
            if out == swapB:
                new_gates.append([a, gate, b, swapA])
                changes = True
                break
        if not changes:
            new_gates.append([a, gate, b, out])

    wire_values = simulate(wire_values, new_gates)



    for a, gate, b, out in gates:
        graph.edge(a, out, f'{gate}{wire_values[a]}')
        graph.edge(b, out, f'{gate}{wire_values[b]}')

    for wire, value in wire_values.items():
        if value == 1:
            graph.node(wire, wire, style='filled', fillcolor='green')


    x = extract_output(wire_values, "x")
    y = extract_output(wire_values, "y")
    z_bin = bin(x+y)[2:]
    print(x, y, z_bin)

    # Create the dictionary
    binary_length = len(z_bin)
    binary_dict = {
        f"z{str(binary_length - i - 1).zfill(2)}": int(bit)
        for i, bit in enumerate(z_bin)
    }


    z_wires = {wire: value for wire, value in wire_values.items() if wire.startswith("z")}
    print(z_wires)
    print(binary_dict)

    incorrect_wires = []
    for wire, value in binary_dict.items():
        if wire in z_wires:
            if z_wires[wire] != value:
                incorrect_wires.append((wire, z_wires[wire]))

    for wire, value in incorrect_wires:
        graph.node(wire, wire, style='filled', fillcolor='red')

    print(incorrect_wires)
    graph.render(directory=Path("outputs/graphviz"))

    if len(incorrect_wires) == 0:
        return ",".join(sorted([item for sublist in swaps for item in sublist]))





with open('2024-24-Crossed_Wires.txt') as f:
    wires, gates = f.read().split("\n\n")
    wire_values = {name.strip(): int(value.strip()) for wire in wires.splitlines() for name, value in [wire.split(":")]}
    OGvals = deepcopy(wire_values)
    gates = [gate.replace(" -> ", " ").split() for gate in gates.splitlines()]
    print(gates)

    # part 1
    new_wire_values = simulate(wire_values, gates)
    print("Part1",extract_output(new_wire_values, "z"))

    #part 2
    print(find_swaps(OGvals, gates))
