from stockfish import Stockfish

class Computer:
    def __init__(self, skill_level):
        self.engine = Stockfish("./stockfish12/bin/stockfish")
        self.engine.set_skill_level(skill_level)
        self.move_history = []

    def get_move(self, player_move):
        self.move_history.append(player_move)
        self.engine.set_position(self.move_history)
        auto_move = self.engine.get_best_move()
        self.move_history.append(auto_move)

        return auto_move

    def print_board(self):
        self.engine.set_position(self.move_history)
        print(self.engine.get_board_visual())

# input -- board state (changes based on the user's move)

# output -- stockfish move