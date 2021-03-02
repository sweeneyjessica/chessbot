from engine import Computer
import chess
import chess.svg
import time
import sys
import webbrowser
import sounddevice as sd
import scipy.io.wavfile as wav
from wit import Wit
import time


blank = {'_text': '', 'entities': {}}
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

board = chess.Board()
opponent = Computer(10)
opponent.print_board()

if __name__ == "__main__":
    piece_mapping = {'king':'K', 'queen':'Q', 'knight':'N', 'bishop':'B', 'rook':'R', 'pawn':''}


    sample_rate = 44100
    sd.default.samplerate = sample_rate

    duration = 4  # record for three seconds

    access_token = "WF7LRTYFMA6VOCP7ORHYDDE464DTUC2I"

    client = Wit(access_token)

    while not board.is_checkmate():
        chessboardSvg = chess.svg.board(board)
        f1 = open('test.svg','w')
        f1.write(chessboardSvg)
        f1.close()

        # MacOS

        webbrowser.get(chrome_path).open('test.svg')

        time.sleep(3)

        print("Make a move:")

        myrecording = sd.rec(duration * sample_rate, channels=1)
        sd.wait()

        wav.write("output_sound.wav", sample_rate, myrecording)  # create wav file

        with open("output_sound.wav", "rb") as f:
            resp = client.speech(f, {'Content-Type': 'audio/wav'})  # send to wit


        print(resp)

        if resp == blank:
            print("Sorry I didn't get that")
            continue

        try:
            if 'piece:capturer' in resp['entities']:
                piece = resp['entities']['piece:capturer'][0]['value']
                square = resp['entities']['square:square'][0]['value']

                san_move = "{}{}".format(piece_mapping[piece], square)
            else:
                square = resp['entities']['square:square'][0]['value']

                san_move = square
        except:
            print("Sorry I didn't get that")
            continue
            #san_move = input()

        try:
            move = board.push_san(san_move)
            uci_move = move.uci()
        except:
            continue

        auto_move = opponent.get_move(uci_move)
        board.push(chess.Move.from_uci(auto_move))

        opponent.print_board()

    

