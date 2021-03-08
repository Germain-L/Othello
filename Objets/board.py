from .pawn import Pawn

class Board:
    def __init__(self, size):
        self.size = size
        self.generate()

    def generate(self):
        #TODO DELETE
        self.size += 2
        rows = ["•" for i in range(self.size)]
        self.board = [rows for i in range(self.size)]

    #TODO DELETE
    def display(self):
        for x in range(self.size):
            for y in range(self.size):
                print(self.board[x][y])

    def place(self, x, y, pawn):
        #TODO place pawn in a case
        pass
    
    def check(self, x, y):
        #TODO check if pawn eat other pawns
        pass

    def replace(self, x, y, pawn):
        #TODO replace pawn by other color
        pass

