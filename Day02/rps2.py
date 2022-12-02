"""
Allister MacLeod - Advent of Code Day 2
Rock Paper Scissors - playing for outcomes

"""

import fileinput
import roshambo


class RPS(object):
    def __init__(self, lines: list[str]):
        (self.opponent_moves, self.desired_outcomes) = self.parse(lines)

    @staticmethod
    def parse(lines: list[str]) -> (list[str], list[int]):
        moves = []
        outcomes = []
        for line in lines:
            parts = line.strip().split(' ')
            if len(parts) == 2:
                moves.append(roshambo.strategy_move(parts[0]))
                outcomes.append(roshambo.strategy_outcome(parts[1]))
        return moves, outcomes

    def total_score(self) -> int:
        score = 0
        for (opponent_move, outcome) in zip(self.opponent_moves, self.desired_outcomes):
            my_move = roshambo.play_for_outcome(opponent_move, outcome)
            score += roshambo.game_score(opponent_move, my_move)
        return score
    

def main():
    rps = RPS([line for line in fileinput.input()])
    print(rps.total_score())


if __name__ == '__main__':
    main()
