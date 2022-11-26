class DeterministicDice:
    def __init__(self):
        self.numbers = list(range(1, 101))
        self.currentIdx = 0
        self.rolls = 0

    def roll(self):
        if self.currentIdx == len(self.numbers):
            self.currentIdx = 0

        value = self.numbers[self.currentIdx]
        self.currentIdx += 1
        self.rolls += 1

        return value


def play(players, dice):
    next_value = 1
    while True:
        for player in players:
            turn_moves = 0
            description = f"Player {player['player']} rolls "
            for _ in range(0, 3):
                roll = dice.roll()

                description += f"{roll} + "
                turn_moves += roll

            description = description[:-2]
            next_value += 3

            new_position = (player.get("position") + turn_moves) % 10
            if new_position == 0:
                new_position = 10

            player["position"] = new_position
            player["score"] += player["position"]

            description += f" and moves to space {player['position']} for a total score of {player['score']}"
            print(description)

            if player["score"] >= 1000:
                #game over
                return dice.rolls

def score_game(players, dice_rolled):
    min_score = 10000000
    for player in players:
        if player["score"] < min_score:
            min_score = player["score"]

    return min_score * dice_rolled


def part1():
    players = [
        {
            "player": 1,
            "position": 5,
            "score": 0
        },
        {
            "player": 2,
            "position": 9,
            "score": 0
        }
    ]
    dice = DeterministicDice()
    dice_rolled = play(players, dice)

    print(f"Day 21, part 1: {score_game(players, dice_rolled)}")


if __name__ == '__main__':
    part1()