from Objets.board import Board
from Objets.pawn import Pawn


def main():
    board = Board(8)
    whose_turn = True

    while True:
        print(board)

        if whose_turn:
            print("x's turn")
            board.new_pawn(Pawn(1))

        else:
            print("o's turn")
            board.new_pawn(Pawn(0))

        whose_turn = not whose_turn
        # if board.check_end():
            # break


if __name__ == '__main__':
    main()
