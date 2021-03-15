from .pawn import Pawn


class Board:
    def __init__(self, size):
        self.size = size
        self.generate()
        self.start()

    def generate(self):
        # TODO DELETE
        self.board = [["•"] * self.size for _ in range(self.size)]

    def display(self):
        """Displays the board in a grid"""
        # TODO DELETE

        nums = [i for i in range(1, self.size + 1)]

        print(" ", end="")
        for i in nums:
            print(f" {i}", end="")
        print()

        for x in range(len(self.board)):
            print(nums[x], end=" ")
            for y in range(len(self.board[x])):
                print(self.board[x][y], end=" ")
            print()

    def start(self):
        x = (self.size // 2) - 1
        y = (self.size // 2) - 1
        self.place(x, y, Pawn(0))
        self.place(x + 1, y, Pawn(1))
        self.place(x, y + 1, Pawn(1))
        self.place(x + 1, y + 1, Pawn(0))

    def place(self, x, y, pawn):
        self.board[x][y] = pawn.view()

    def check(self, x, y):
        # TODO check if pawn eat other pawns
        pass

    def replace(self, x, y, pawn):
        # TODO replace pawn by other color
        pass

    def new_pawn(self, pawn):
        """Lets the user input coordinates to place a pawn"""

        allowed = [i for i in range(0, self.size)]

        y = ""
        x = ""

        while x not in allowed or y not in allowed:
            y = input('enter x coordinate for new pawn: ')
            x = input('enter y coordinate for new pawn: ')

            try:
                x = int(x) - 1
                y = int(y) - 1

                if x not in allowed or y not in allowed:
                    print(f"Please make sure to enter numbers between 1 and {self.size}")

            except ValueError:
                print(f"Please make sure to enter numbers only")

            if self.board[x][y] in ["x", "o"]:
                y = ""
                x = ""

                print("Invalid coordinates pawn already present")

        self.place(x, y, pawn)
        print(f"Added pawn in {x}, {y}")

    def check_end(self):
        contains_white = False
        contains_black = False

        white_count = 0
        black_count = 0

        full = True

        for x in range(len(self.board)):
            if "•" in self.board[x]:
                full = False
            for y in range(len(self.board[x])):
                current_pawn = self.board[x][y]
                if type(current_pawn) == Pawn:
                    if current_pawn.color == 0:
                        white_count += 1
                        contains_white = True

                    elif current_pawn.color == 1:
                        black_count += 1
                        contains_black = True

        if contains_white and not contains_black:
            print("Blanc gagne")
            return True

        elif contains_black and not contains_white:
            print("Noir gagne")
            return True

        elif full:
            if contains_white > contains_black:
                print("Blanc gagne")
                return True

            elif contains_black > contains_white:
                print("Noir gagne")
                return True

            else:
                print("Execo")
                return True
        return False