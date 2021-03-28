from .board import Board
from .pawn import Pawn, ColoursCodes


class Game:
    def __init__(self, size):
        # initialise the board with its size
        self.game_board = Board(size)

        # x starts the game
        self.is_x_turn = True

    @property
    def game_board(self):
        return self.__game_board

    @game_board.setter
    def game_board(self, board):
        self.__game_board = board

    @property
    def is_x_turn(self) -> bool:
        return self.__is_x_turn

    @is_x_turn.setter
    def is_x_turn(self, is_x_turn):
        # this property to determins who's turn it is
        self.__is_x_turn = is_x_turn

    def turn(self):
        if self.is_x_turn:
            # print play's turn in corresponding color
            print(f"{ColoursCodes.GREEN} x's turn {ColoursCodes.END}")

            self.game_board.new_pawn(Pawn(0))

        elif not self.is_x_turn:
            # print play's turn in corresponding color
            print(f"{ColoursCodes.RED} o's turn {ColoursCodes.END}")
            self.game_board.new_pawn(Pawn(1))

        self.is_x_turn = not self.is_x_turn

    def play(self):
        x_score = len(self.game_board.x_pawns)
        o_score = len(self.game_board.o_pawns)

        while not self.game_board.game_ended():
            # diplay the board
            print(self.game_board)

            # execute new turn
            self.turn()

            x_score = len(self.game_board.x_pawns)
            o_score = len(self.game_board.o_pawns)

            print("\n=====================\n")
            # print the scores
            print("SCORE :", end="\n")
            print(f"    x : {x_score}")
            print(f"    o : {o_score}\n")

        print(self.game_board)

        if x_score > o_score:
            print("x WINS")
        elif x_score < o_score:
            print("o WINS")
        else:
            print("DRAW")
