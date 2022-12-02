"""

"""

LOSS = -1
DRAW = 0
WIN = 1

# from perspective of first player
outcome_table = [
    ('rock', 'rock', DRAW),
    ('rock', 'paper', LOSS),
    ('rock', 'scissors', WIN),
    ('paper', 'rock', WIN),
    ('paper', 'paper', DRAW),
    ('paper', 'scissors', LOSS),
    ('scissors', 'rock', LOSS),
    ('scissors', 'paper', WIN),
    ('scissors', 'scissors', DRAW)
]

by_moves = {}
for (p1, p2, outcome) in outcome_table:
    by_moves[(p1, p2)] = outcome

by_desired_outcome = {}
for (p1, p2, outcome) in outcome_table:
    by_desired_outcome[(p2, outcome)] = p1


def strategy_move(strategy: str) -> str:
    return {'A': 'rock', 'B': 'paper', 'C': 'scissors'}[strategy]


def strategy_counter(counter: str) -> str:
    return {'X': 'rock', 'Y': 'paper', 'C': 'scissors'}[counter]


def move_score(move: str) -> int:
    return {'rock': 1, 'paper': 2, 'scissors': 3}[move]


def outcome_score(outcome: int) -> int:
    return {-1: 0, 0: 3, 1: 6}[outcome]


def game_outcome(opponent_move: str, player_move: str) -> int:
    """
    Calculate the outcome of an RPS round, from the perspective
    of player_move.

    :return:  -1 for loss, 0 for draw, 1 for victory
    """
    return by_moves[(player_move, opponent_move)]


def play_for_outcome(opponent_move: str, desired_outcome: int) -> str:
    return by_desired_outcome[(opponent_move, desired_outcome)]
