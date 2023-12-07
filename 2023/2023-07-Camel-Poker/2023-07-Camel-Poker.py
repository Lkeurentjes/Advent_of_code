from collections import Counter
def type(hand):
    c = Counter(hand)
    if 5 in c.values():
        return "Five of a kind"
    elif 4 in c.values():
        return "Four of a kind"
    elif 3 in c.values() and 2 in c.values():
        return "Full house"
    elif 3 in c.values():
        return "Three of a kind"
    elif 2 in c.values():
        v = Counter(c.values())
        if 3 in v.values():
            return "One pair"
        return "Two pair"
    return "High card"

def joker(hand, ranks):
    c = Counter(hand)

    def get_rank(card):
        return ranks[card]

    joker_count = c.pop('J', 0)
    if joker_count > 0 and joker_count!= 5:
        joker_value = [card for card in c if c[card] == max(c.values()) and get_rank(card) == max(get_rank(card) for card in c if c[card] == max(c.values()))][0]
        hand = hand.replace('J', joker_value, joker_count)
    return hand


def sort_poker_hands(hands, ranks):
    def poker_sort_key(item):
        hand, score = item
        key = [ranks[card] for card in hand]
        return (tuple(key), score)
    return sorted(hands, key=poker_sort_key, reverse=True)

with open('2023-07-Camel-Poker.txt') as f:
    lines = f.read().splitlines()
    hands = [(line.split()[0], int(line.split()[1])) for line in lines]

poker_hands = {
    "Five of a kind": [],
    "Four of a kind": [],
    "Full house": [],
    "Three of a kind": [],
    "Two pair": [],
    "One pair": [],
    "High card": []
}

poker_hands_joker_version = {
    "Five of a kind": [],
    "Four of a kind": [],
    "Full house": [],
    "Three of a kind": [],
    "Two pair": [],
    "One pair": [],
    "High card": []
}


ranks_standard = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
ranks_joker = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

for hand, score in hands:
    poker_hands[type(hand)].append((hand,score))
    poker_hands_joker_version[type(joker(hand, ranks_joker))].append((hand,score))

for i, (p_hands, ranks) in enumerate([(poker_hands, ranks_standard),(poker_hands_joker_version,ranks_joker)]):
    totalhands = len(hands)
    score = 0
    for key, value in p_hands.items():
        valuesorted = sort_poker_hands(value, ranks)
        for h, b in valuesorted:
            score += totalhands * b
            totalhands -= 1
    print("Part",i,"has a score of",score)

