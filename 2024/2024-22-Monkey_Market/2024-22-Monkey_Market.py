from collections import defaultdict

def generate_secret(secret, Modulo, steps=2000):
    for _ in range(steps):
        secret ^= (secret * 64) % Modulo # multiplied by 64, reduced by modulo XORed with the current secret
        secret ^= (secret // 32) % Modulo # divided by 32, reduced by modulo XORed with the current secret
        secret ^= (secret * 2048) % Modulo # multiplied by 2048, reduced by modulo XORed with the current secret
    return secret

def generate_price_changes(secret, Modulo, steps=2000):
    # calculate prices
    prices = []
    for _ in range(steps+1):
        price = secret % 10 # get last number
        prices.append(price)

        secret ^= (secret * 64) % Modulo
        secret ^= (secret // 32) % Modulo
        secret ^= (secret * 2048) % Modulo
        secret %= Modulo

    # Calculate changes between consecutive prices
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i - 1])

    return prices, changes

def find_best_buy(secrets, Modulo, steps=2000):
    # get all scores and compare
    sequence_scores = defaultdict(int)
    for secret in secrets:
        prices, changes = generate_price_changes(secret, Modulo, steps)
        visited = set()
        for i in range(len(changes)-3):
            seq = tuple(changes[i :i + 4])
            # only use the first occurrence
            if seq not in visited:
                visited.add(seq)
                sequence_scores[seq] += prices[i + 4] % 10

    # find best score based on number of banana's
    best_sequence = max(sequence_scores, key=sequence_scores.get)
    bananas = sequence_scores[best_sequence]
    return best_sequence, bananas


with open('2024-22-Monkey_Market.txt') as f:
    secrets = [int(s) for s in f.read().splitlines()]
    result = sum(generate_secret(initial, 16777216, steps=2000) for initial in secrets)
    print("Part 1, sum of the 2000 secret is,", result)
    seq, bananas = find_best_buy(secrets, 16777216, steps=2000)
    print("Part 2, best sequence to sell is", seq, "which sells for", bananas, "bananas")

