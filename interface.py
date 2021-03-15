from engine import Computer
import chess
import chess.svg
from recorder import record
from cairosvg import svg2png
from DialogFrameSimple import DialogFrameSimple
import pprint

def write_png(chessboard, start = None, end = None):
    if start == None:
        chessboardSvg = chess.svg.board(chessboard)
        svg2png(bytestring=chessboardSvg,write_to='test.png')
    else:
        displaySuggestedMove = chess.svg.board(chessboard, arrows=[chess.svg.Arrow(start, end)])
        svg2png(bytestring=displaySuggestedMove,write_to='test.png')


class FrameDM:

    def __init__(self, NLU, NLG):
        self.NLU = NLU
        self.NLG = NLG
        self.DialogFrame = DialogFrameSimple()

    def play_game(self, opp_type, opp_level):

        self.DialogFrame.opponent_type = opp_type
        if opp_type == 'computer':
            if opp_level == 'easy':
                self.DialogFrame.computer_engine = Computer(1)
            elif opp_level == 'medium':
                self.DialogFrame.computer_engine = Computer(5)
            elif opp_level == 'hard':
                self.DialogFrame.computer_engine = Computer(10)
            else:
                self.DialogFrame.computer_engine = Computer(1)

        self.DialogFrame.board_obj = chess.Board()
        write_png(self.DialogFrame.board_obj)

        while not self.DialogFrame.board_obj.is_checkmate():

            if self.DialogFrame.misunderstood_times < 2:
                resp = record()
                #pprint.pprint(resp)
                intent, text, slots = self.NLU.parse(resp)
            else:
                utterance = input("Please type your move or request:")
                intent, text, slots = self.NLU.parse_text(utterance)
                self.DialogFrame.misunderstood_times = 0

            output = self.execute(intent, text, slots) # updates frame and generates NLG response
            #print(output)

    def execute(self, intent, text, slots):

        if intent == "confirm":
            if self.DialogFrame.request_best_move:
                user_move = self.DialogFrame.board_obj.san(self.DialogFrame.suggested_move)
                self.DialogFrame.request_best_move = False
                self.DialogFrame.suggested_move = None

                self.DialogFrame.misunderstood_times = 0

        elif intent == 'deny':
            if self.DialogFrame.request_best_move:
                self.DialogFrame.request_best_move = False
                self.DialogFrame.suggested_move = None

                self.DialogFrame.misunderstood_times = 0

                return self.NLG.generate('prompt_move')

        elif intent == "request_best_move":
            suggested_move = self.DialogFrame.computer_engine.get_suggestion()
            start_square = chess.Move.from_uci(suggested_move).from_square
            end_square = chess.Move.from_uci(suggested_move).to_square
            self.DialogFrame.suggested_move = suggested_move

            write_png(self.DialogFrame.board_obj, start_square, end_square)

            self.DialogFrame.request_best_move = True
            self.DialogFrame.misunderstood_times = 0

            return self.NLG.generate(intent, suggested_move)

        elif intent == "move_piece":
            if self.DialogFrame.clarify:
                if self.DialogFrame.understood_piece is not None:
                    piece = self.DialogFrame.understood_piece
                    if slots['square'] != 'unclear':
                        square = slots['square']
                        self.DialogFrame.clarify = False
                    else:
                        self.DialogFrame.clarify = True
                        self.DialogFrame.misunderstood_times += 1

                        return self.NLG.generate('clarify', 'square')
                elif self.DialogFrame.understood_square is not None:
                    square = self.DialogFrame.understood_square
                    if slots['piece'] != 'unclear':
                        piece = slots['piece']
                        self.DialogFrame.clarify = False
                    else:
                        self.DialogFrame.clarify = True
                        self.DialogFrame.misunderstood_times += 1

                        return self.NLG.generate('clarify', 'piece')
                else:
                    if slots['piece'] != 'unclear':
                        piece = slots['piece']
                        self.DialogFrame.understood_piece = piece
                    if slots['square'] != 'unclear':
                        square = slots['square']
                        self.DialogFrame.understood_square = square

                    if self.DialogFrame.understood_square is None:
                        self.DialogFrame.clarify = True
                        self.DialogFrame.misunderstood_times += 1

                        return self.NLG.generate('clarify', 'square')

                    if self.DialogFrame.understood_piece is None:
                        self.DialogFrame.clarify = True
                        self.DialogFrame.misunderstood_times += 1

                        return self.NLG.generate('clarify', 'piece')
            else:
                if slots['piece'] == 'unclear':
                    self.DialogFrame.clarify = True
                    if slots['square'] != 'unclear':
                        self.DialogFrame.understood_square = slots['square']

                    self.DialogFrame.clarify = True
                    self.DialogFrame.misunderstood_times += 1

                    return self.NLG.generate('clarify', 'piece')
                else:
                    piece = slots['piece']
                if slots['square'] == 'unclear':
                    if slots['piece'] != 'unclear':
                        self.DialogFrame.understood_piece = slots['piece']

                    self.DialogFrame.clarify = True
                    self.DialogFrame.misunderstood_times += 1

                    return self.NLG.generate('clarify', 'square')
                else:
                    square = slots['square']

            user_move = "{}{}".format(self.DialogFrame.piece_mapping[piece], square)

            self.DialogFrame.understood_piece = None
            self.DialogFrame.understood_square = None
            self.DialogFrame.clarify = False
            self.DialogFrame.misunderstood_times = 0

        else:
            self.DialogFrame.misunderstood_times += 1
            return self.NLG.generate('misunderstood')

        try:
            move = self.DialogFrame.board_obj.push_san(user_move)
            uci_move = move.uci()
            write_png(self.DialogFrame.board_obj)
        except:
            return self.NLG.generate('invalid_move')

        self.DialogFrame.move_history.append(uci_move)

        if self.DialogFrame.opponent_type == 'computer':
            auto_move = self.DialogFrame.computer_engine.get_move(uci_move)
            self.DialogFrame.board_obj.push(chess.Move.from_uci(auto_move))
            self.DialogFrame.move_history.append(auto_move)

            write_png(self.DialogFrame.board_obj)

            return self.NLG.generate('successful_turn', auto_move)