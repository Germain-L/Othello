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

    def start(self):
        x = (self.size / 2) - 1
        y = (self.size / 2) - 1
        self.place(x, y, Pawn(0))
        self.place(x+1, y, Pawn(1))
        self.place(x, y+1, Pawn(1))
        self.place(x+1, y+1, Pawn(0))

    def place(self, x, y, pawn):
        #TODO place pawn in a case
        pass
    
    def check(self, x, y):
        #TODO check if pawn eat other pawns
        pass

    def replace(self, x, y, pawn):
        #TODO replace pawn by other color
        pass

