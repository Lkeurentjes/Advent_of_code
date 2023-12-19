from copy import deepcopy
def generate_Lambda(flow):  # wel sad this is to good for part 2
    flow = flow.split(",")
    lambdastr = "lambda x, m, a, s: "
    for f in flow:
        if ":" in f:
            condition, label = f.split(':')
            lambdastr += "'" + label + "' if " + condition + " else "
        else:
            lambdastr += "'" + f + "'"
    return eval(lambdastr)


lambdadict = {}
stringdict = {}
with open('2023-19-Aplenty.txt') as f:
    flows, parts = f.read().split("\n\n")
    parts = [
        eval(part.replace("=", ":").replace("x", "'x'").replace("m", "'m'").replace("a", "'a'").replace("s", "'s'")) for
        part in parts.split("\n")]
    for flow in flows.split("\n"):
        name, function = flow.split("{")
        lambdadict[name] = generate_Lambda(function[:-1])
        stringdict[name] = function[:-1].split(",")

sumpt1 = 0
for part in parts:
    flowname = "in"
    while (flowname != "A" and flowname != "R"):
        flowname = lambdadict[flowname](part["x"], part["m"], part["a"], part["s"])
    if flowname == "A":
        sumpt1 += part["x"] + part["m"] + part["a"] + part["s"]
print("Print for part 1 the answer is: ", sumpt1)


def end_sum(xmas):
    m = 1
    for s, e in xmas.values():
        m *= (e - s + 1)
    return m

def recursive_range_run(xmas, flowname):
    rangesum = 0
    for condition in stringdict[flowname]:
        if ":" in condition:
            con, to = condition.split(":")
            if ">" in con:
                val, num = con.split(">")
                newXmas = deepcopy(xmas)
                if newXmas[val][1] > int(num):
                    newXmas[val][0] = max(xmas[val][0], int(num) + 1)
                    if to == "A":
                        rangesum += end_sum(newXmas)
                    elif to != "R":
                        rangesum += recursive_range_run(newXmas, to)
                    xmas[val][1] = min(xmas[val][1], int(num))
            if "<" in con:
                val, num = con.split("<")
                newXmas = deepcopy(xmas)
                if newXmas[val][0] < int(num):
                    newXmas[val][1] = min(xmas[val][1], int(num) - 1)
                    if to == "A":
                        rangesum += end_sum(newXmas)
                    elif to != "R":
                        rangesum += (recursive_range_run(newXmas, to))
                    xmas[val][0] = max(xmas[val][0], int(num))
        else:
            if condition == "A":
                rangesum += end_sum(xmas)
            elif condition != "R":
                rangesum += recursive_range_run(xmas, condition)
    return rangesum

print("Print for part 2 the answer is: ",
      recursive_range_run({"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}, "in"))

