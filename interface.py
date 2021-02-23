from engine import Computer
import chess

game = chess.Board()
opponent = Computer(10)

if __name__ == "__main__":
    while not game.is_checkmate():
        print("Make a move:")
        move = input()

        if move == "quit":
            break

        try:
            move = game.push_san(move)
            uci_move = move.uci()
        except:
            continue

        auto_move = opponent.get_move(uci_move)
        game.push(chess.Move.from_uci(auto_move))

        opponent.print_board()

