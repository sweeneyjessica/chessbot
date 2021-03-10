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
from recorder import record
from cairosvg import svg2png
from PIL import Image
import subprocess
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from NLU import NLUDefault

def play_game(opp_type):
    blank = {'_text': '', 'entities': {}}
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    board = chess.Board()

    opponent = Computer(10)
    #opponent.print_board()

    piece_mapping = {'king':'K', 'queen':'Q', 'knight':'N', 'bishop':'B', 'rook':'R', 'pawn':''}

    chessboardSvg = chess.svg.board(board)
    svg2png(bytestring=chessboardSvg,write_to='test.png')

    NLU = NLUDefault()

    while not board.is_checkmate():

        resp = record()
        intent, text, slots = NLU.parse(resp)
        print(intent)
        print(text)
        print(slots)

        try:
            print(resp['intents'][0]['name'])
            if resp['intents'][0]['name'] == 'take_back':
                board.pop()
                board.pop()
                continue

            if resp['intents'][0]['name'] == 'request_best_move':
                suggested_move = opponent.get_suggestion()
                start_square = chess.Move.from_uci(suggested_move).from_square
                end_square = chess.Move.from_uci(suggested_move).to_square

                #viewer.kill()
                displaySuggestedMove = chess.svg.board(board, arrows=[chess.svg.Arrow(start_square, end_square)])
                svg2png(bytestring=displaySuggestedMove,write_to='test.png')

                # f1 = open('test.svg', 'w')
                # f1.write(displaySuggestedMove)
                # f1.close()

                #webbrowser.get(chrome_path).open('test.svg')

                continue

            if 'piece:capturer' in resp['entities']:
                piece = resp['entities']['piece:capturer'][0]['value']
                square = resp['entities']['square:square'][0]['value']

                san_move = "{}{}".format(piece_mapping[piece], square)
            else:
                square = resp['entities']['square:square'][0]['value']

                san_move = square
        except:
            print("Sorry I didn't get that, try 'alpha four' or 'queen delta two'")
            print('''A as in Alpha
B as in Bravo
C as in Charlie
D as in Delta
E as in Echo
F as in Foxtrot or Foot (foxtrot doesn't work very well)
G as in Golf or Gamma
H as in Hotel''')
            continue
            #san_move = input()

        try:
            move = board.push_san(san_move)
            uci_move = move.uci()
            #opponent.print_board()
        except:
            print('Invalid move')
            continue

        if opp_type == 'computer':
            auto_move = opponent.get_move(uci_move)
            board.push(chess.Move.from_uci(auto_move))


        #viewer.kill()
        chessboardSvg = chess.svg.board(board)
        svg2png(bytestring=chessboardSvg,write_to='test.png')
        #viewer = subprocess.Popen(['open','test.png'])
        # chessboardSvg = chess.svg.board(board)
        # f1 = open('test.svg', 'w')
        # f1.write(chessboardSvg)
        # f1.close()

        # MacOS

        #webbrowser.get(chrome_path).open('test.svg')

    

