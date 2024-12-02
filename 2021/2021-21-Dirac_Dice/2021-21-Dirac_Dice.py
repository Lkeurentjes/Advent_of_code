from functools import lru_cache


class Game:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.score1 = 0
        self.score2 = 0

        self.die = 0
        self.roll = 0

    def roll_deterministic(self):
        self.die = self.die + 1 if self.die < 100 else 1
        self.roll += 1
        return self.die

    def play(self):
        while self.score1 < 1000 and self.score2 < 1000:
            # PLAYER 1
            # roll 3 times
            steps = self.roll_deterministic() + self.roll_deterministic() + self.roll_deterministic()
            self.pos1 = (self.pos1 + steps - 1) % 10 + 1
            self.score1 += self.pos1

            if self.score1 >= 1000:
                break

            # PLAYER 2
            # roll 3 times
            steps = self.roll_deterministic() + self.roll_deterministic() + self.roll_deterministic()
            self.pos2 = (self.pos2 + steps - 1) % 10 + 1
            self.score2 += self.pos2

        return min(self.score1, self.score2) * self.roll

    def play_quantum(self, startone, starttwo):

        @lru_cache(maxsize=None)
        def quantum_turn(pos1, score1, pos2, score2, is_player1_turn):
            if score1 >= 21:
                return (1, 0)  # Player 1 wins in this universe
            if score2 >= 21:
                return (0, 1)  # Player 2 wins in this universe

            rolls = [1, 2, 3]
            outcomes = [sum([r1, r2, r3]) for r1 in rolls for r2 in rolls for r3 in rolls]

            universe_score = (0,0)

            for outcome in outcomes:
                if is_player1_turn:
                    new_pos1 = (pos1 + outcome - 1) % 10 + 1
                    new_score1 = score1 + new_pos1
                    wins1, wins2 = quantum_turn(new_pos1, new_score1, pos2, score2, False)
                else:
                    new_pos2 = (pos2 + outcome - 1) % 10 + 1
                    new_score2 = score2 + new_pos2
                    wins1, wins2 = quantum_turn(pos1, score1, new_pos2, new_score2, True)

                universe_score = (universe_score[0] + wins1, universe_score[1] + wins2)

            return universe_score


        return quantum_turn(startone, 0, starttwo, 0, True)


with open('2021-21-Dirac_Dice.txt') as f:
    lines = f.read().splitlines()
    playerOne = int(lines[0].split()[-1])
    playerTwo = int(lines[1].split()[-1])
    Direc = Game(playerOne, playerTwo)
    print("Part 1, lowest score * rolls =", Direc.play())
    wins1, wins2 = Direc.play_quantum(playerOne, playerTwo)

    print(f"Part 2: The player who wins in more universes wins in {max(wins1, wins2)} universes.")
    print(f"\tPlayer 1 wins in {wins1} universes.")
    print(f"\tPlayer 2 wins in {wins2} universes.")
