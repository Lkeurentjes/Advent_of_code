def check_password(min, max, part, password):
    return min <= password.count(part) <= max

def check_possitions(min, max, part, password):
    return (password[min-1] == part) != (password[max-1] == part)

with open('2020-02-Password_Philosophy.txt') as f:
    lines = f.read().splitlines()
    data = [[int(part) if i < 2 else part
             for i, part in enumerate(f.replace(":", " ").replace("-", " ").split())]
            for f in lines
            ]
    print(data)
    correct = 0
    correct_positions = 0
    for min,max,part,password in data:
        if check_password(min, max, part, password): correct += 1
        if check_possitions(min, max, part, password): correct_positions += 1
    print("Part 1, number of correct passwords",correct)
    print("Part 2, number of correct passwords", correct_positions)
