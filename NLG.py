

class NLGDefault:
    def __init__(self):
        self.Name = "NLGDefault"

    def generate(self, intent, more_info):
        if intent == 'request_best_move':
            return "The best move here is: {}\nDo you want to play this move?".format(more_info)

        elif intent == 'clarify':
            if more_info == 'piece':
                return "What piece do you want to move?"
            elif more_info == 'square':
                return "What square do you want to move to?"

        elif intent == 'invalid_move':
            return "That move is invalid, try again."

        elif intent == 'successful_turn':
            return "The computer made this move: {}\nWhat move do you want to play now?".format(more_info)

        elif intent == 'prompt_move':
            return "What move do you want to play now?"

        elif intent == 'misunderstood':
            return "I'm not sure what you said. Can you repeat?"





        # clarifying questions
        #   if two pieces could make a move, specify which
        #   if move wasn't heard correctly (or at all), ask to restate
        #   if move is illegal, ask for new move

        # responding with computer's move

        # responding with best engine move
        # asking if they want to play the best engine move

