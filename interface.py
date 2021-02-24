from engine import Computer
import chess
import chess.svg
import time
import sys
import webbrowser

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

board = chess.Board()
opponent = Computer(10)
opponent.print_board()

if __name__ == "__main__":
    while not board.is_checkmate():
        chessboardSvg = chess.svg.board(board)
        f1 = open('test.svg','w')
        f1.write(chessboardSvg)
        f1.close()

        # MacOS
        

        webbrowser.get(chrome_path).open('test.svg')


        



        print("Make a move:")
        move = input()

        if move == "quit":
            break

        try:
            move = board.push_san(move)
            uci_move = move.uci()
        except:
            continue

        auto_move = opponent.get_move(uci_move)
        board.push(chess.Move.from_uci(auto_move))

        opponent.print_board()

    

