"""
Allister MacLeod - Advent of Code Day 2
Rock Paper Scissors

"""

import fileinput
import roshambo


class RockPaperScissors(object):
    def __init__(self, strategy_guide: list[str]):
        (self.opponent, self.own) = RockPaperScissors.parse(strategy_guide)

    @staticmethod
    def round_score(opponent_move: str, my_move: str) -> int:
        move_score = roshambo.move_score(my_move)
        victory_score = roshambo.outcome_score(roshambo.game_outcome(opponent_move, my_move))
        return move_score + victory_score

    @staticmethod
    def parse(lines: list[str]) -> (list[str], list[str]):
        opponent_moves = []
        my_moves = []
        for line in lines:
            parts = line.strip().split(' ')
            if len(parts) == 2:
                opponent_moves.append(roshambo.strategy_move(parts[0]))
                my_moves.append(roshambo.strategy_counter(parts[1]))
        return opponent_moves, my_moves

    def total_score(self) -> int:
        score = 0
        for (opponent, mine) in zip(self.opponent, self.own):
            score += RockPaperScissors.round_score(opponent, mine)
        return score


def main():
    strategy = [line for line in fileinput.input()]
    rps = RockPaperScissors(strategy)
    score = rps.total_score()
    print(score)


if __name__ == '__main__':
    main()
