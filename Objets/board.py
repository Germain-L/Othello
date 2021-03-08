from .pawn import Pawn

class Board:
    def __init__(self, size):
        self.size = size
        self.generate()

    def generate(self):
        #TODO DELETE
        rows = ["•" for i in range(self.size)]
        self.board = [rows for i in range(self.size)]

    def display(self):
        """Displays the board in a grid"""
        #TODO DELETE

        nums = [i for i in range(1, self.size +1)]
        
        print(" ", end="")
        for i in nums:
            print(f" {i}", end="")
        print()

        for x in range(len(self.board)):
            print(nums[x], end=" ")

            for y in range(len(self.board[x])):
                print(self.board[x][y], end=" ")
            print()

    def place(self, x, y, pawn):
        #TODO place pawn in a case
        pass
    
    def check(self, x, y):
        #TODO check if pawn eat other pawns
        pass

    def replace(self, x, y, pawn):
        #TODO replace pawn by other color
        pass

