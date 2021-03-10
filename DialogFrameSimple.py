

class DialogFrameSimple:

    def __init__(self):
        self.move_history = []
        self.board_obj = None
        self.opponent_type = None
        self.computer_engine = None
        self.clarify = False
        self.understood_piece = None
        self.understood_square = None
        self.request_best_move = False
        self.suggested_move = None
        self.piece_mapping = {'king':'K', 'queen':'Q', 'knight':'N', 'bishop':'B', 'rook':'R', 'pawn':'', '':'', None:''}