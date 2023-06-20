class fishschool:
    def __init__(self, fishes, normal = 7, baby = 9):
        self.normal = normal
        self.baby = baby
        self.fish_dict = {}
        for i in range(self.baby):
            self.fish_dict[i] = 0
        for fish in fishes:
            self.fish_dict[fish]+=1

    def breed(self, days):
        for i in range(days):
            copydict = {}
            for j in range(self.baby-1):
                copydict[j] = self.fish_dict[j+1]
            copydict[self.normal-1] += self.fish_dict[0]
            copydict[self.baby - 1] = self.fish_dict[0]
            self.fish_dict = copydict

    def count(self):
        return sum(self.fish_dict.values())

with open('2021-06Lanternfish.txt') as f:
    lines = f.read().splitlines()
    fishtimers = list(map(int, lines[0].split(",")))

school = fishschool(fishtimers)
school.breed(80)
print("Part 1: there are",school.count(), "after 80 days")
school.breed(256-80)
print("Part 2: there are",school.count(), "after 256 days")


