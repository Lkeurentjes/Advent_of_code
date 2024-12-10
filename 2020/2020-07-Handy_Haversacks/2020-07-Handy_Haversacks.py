def contain_color(bag, color, rules):
    if rules[bag] is None:
        return False
    else:
        for inside in rules[bag]:
            if inside[1] == color or contain_color(inside[1], color, rules):
                return True
    return False


def number_bags(bag, rules):
    contain = 0
    if rules[bag] is None:
        return 0
    else:
        for inside in rules[bag]:
            contain += inside[0] * (1 + number_bags(inside[1], rules))
    return contain


with open('2020-07-Handy_Haversacks.txt') as f:
    lines = f.read().splitlines()

    bag_rules = {
        f.split(" contain ")[0].replace(" bags", ""): (
            None if f.split(" contain ")[1] == "no other bags." else [
                (int(item.strip().split(" ", 1)[0]), item.strip().split(" ", 1)[1].rstrip("s"))
                for item in f.split(" contain ")[1]
                .replace(".", "")
                .replace(" bag", "")
                .replace(" bags", "")
                .split(",")
            ]
        )
        for f in lines
    }

    golds = 0
    for bag in bag_rules:
        if contain_color(bag, "shiny gold", bag_rules): golds += 1
    print("part 1, the number of bags with shiny gold bags are", golds)
    print("part 2, shiny gold bag contains", number_bags("shiny gold", bag_rules), "bags")
