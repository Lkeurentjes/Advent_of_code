import numpy as np

class Bingocard:
    def __init__(self, list):
        self.card = self.makeintocard(list)
        self.drawn = np.zeros((5,5))
        self.points = np.sum(self.card)

    def makeintocard(self, list):
        card = []
        for line in list[1:]:
            bline = line.split()
            for i in range(5):
                bline[i] = int(bline[i])
            card.append(bline)
        return np.array(card)

    def find_number(self, number):
        index = np.where(self.card == number)
        if index[0].size == 0:
            return False, self.points
        self.drawn[index[0][0], index[1][0]] = 1
        self.points -= number
        return self.doyouhaveBingo(), self.points

    def doyouhaveBingo(self):
        horizontal = np.sum(self.drawn, axis=0)
        vertical = np.sum(self.drawn, axis=1)
        for i in range(5):
            if horizontal[i] == 5 or vertical[i] ==5:
                return True
        return False


with open('2021-04Giant-Squid.txt') as f:
    lines = f.read().splitlines()

bingo = lines[0].split(",")
cards = []

for i in range(0,len(lines)-1,6):
    cardtxt = lines[1+i:i+7]
    card = Bingocard(cardtxt)
    cards.append(card)

first = True
firstpoints = 0
lastpoints = 0
for number in bingo:
    number = int(number)
    todelete = []
    for card in cards:
        boolean, points = card.find_number(number)
        if boolean:
            if first:
                firstpoints = points * number
                first = False
            if len(cards) == 1 or bingo.index(str(number)) == len(bingo)-1:
                lastpoints = points * number
            todelete.append(card)
    if len(todelete)>0:
        for i in todelete:
            cards.remove(i)

print("PART 1: The points are:", firstpoints)
print("PART 2: The points are:", lastpoints)

