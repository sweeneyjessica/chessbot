import pprint

class NLUDefault:

    def __init__(self):
        self.Intent = None
        self.UnderstoodText = None
        self.Slots = {}

        self.piece_mapping = {'king': 'K', 'queen': 'Q', 'knight': 'N', 'bishop': 'B', 'rook': 'R', 'pawn': ''}
        self.backwards_mapping = {'K':'king', 'Q':'queen', 'N':'knight', 'B':'bishop', 'R':'rook'}

        self.req_best_move = ['best move', 'should', 'optimal', 'recommend', 'recommended',
                              'best', 'top', 'ideal', 'suggest', 'suggested']

    def parse(self, wit_resp):

        self.UnderstoodText = wit_resp['text']

        if wit_resp['intents'] == []:
            return self.Intent, self.UnderstoodText, self.Slots

        self.Intent = wit_resp['intents'][0]['name']

        if self.Intent == 'game_type':
            return self.Intent, self.UnderstoodText, self.Slots

        if self.Intent == 'difficulty':
            return self.Intent, self.UnderstoodText, self.Slots

        if self.Intent == "take_back" or self.Intent == "request_best_move":
            return self.Intent, self.UnderstoodText, self.Slots

        if self.Intent == "confirm" or self.Intent == "deny":
            return self.Intent, self.UnderstoodText, self.Slots


        if self.Intent == "move_piece":
            piece = None
            square = None

            pprint.pprint(wit_resp)

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

    def parse_text(self, utterance):
        self.UnderstoodText = utterance

        utterance = "".join(utterance.lower().split()) # remove internal/external whitespace

        if any(char.isdigit() for char in utterance):
            self.Intent = "move_piece"

            if len(utterance) == 3:
                self.Slots['piece'] = self.backwards_mapping[utterance[0]]
                self.Slots['square'] = utterance[1:3]
            elif len(utterance) == 2:
                self.Slots['piece'] = '' #pawn move
                self.Slots['square'] = utterance
            else:
                self.Slots['piece'] = 'unclear'
                self.Slots['square'] = 'unclear'
        else:
            for key in self.piece_mapping:
                if key in utterance:
                    self.Slots['piece'] = key

            for phrase in self.req_best_move:
                if phrase in utterance:
                    self.Intent = 'request_best_move'

            if "yes" in utterance:
                self.Intent = "confirm"

            elif "no" in utterance:
                self.Intent = "deny"













