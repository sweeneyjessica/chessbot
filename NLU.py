class NLUDefault:

    def __init__(self):
        self.Intent = None
        self.UnderstoodText = None
        self.Slots = {}

        self.piece_mapping = {'king': 'K', 'queen': 'Q', 'knight': 'N', 'bishop': 'B', 'rook': 'R', 'pawn': ''}

    def parse(self, wit_resp):
        self.Intent = wit_resp['intents'][0]['name']
        self.UnderstoodText = wit_resp['text']

        if self.Intent == "take_back" or self.Intent == "request_best_move":
            return self.Intent, self.UnderstoodText, self.Slots

        if self.Intent == "move_piece":
            piece = None
            square = None

            print(wit_resp['entities'])

            if 'piece:capturer' in wit_resp['entities']:
                piece = wit_resp['entities']['piece:capturer'][0]['value']

            if 'square:square' in wit_resp['entities']:
                square = wit_resp['entities']['square:square'][0]['value']

            if piece is not None:
                if piece in self.piece_mapping:
                    self.Slots['piece'] = piece # understood piece
                else:
                    self.Slots['piece'] = 'unclear' # didn't understand piece
            else:
                self.Slots['piece'] = '' # pawn move (no piece name involved)

            if square is not None:
                self.Slots['square'] = square
            else:
                self.Slots['square'] = 'unclear'

            return self.Intent, self.UnderstoodText, self.Slots












