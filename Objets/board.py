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
                if (type(self.board[x][y]) == Pawn):
                    print(self.board[x][y].view(), end=" ")
                else:
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
        self.board[x][y] = pawn
    
    def check(self, x, y, pawn):
        same = []
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if (type(self.board[x][y]) == Pawn 
                and self.board[x][y].color == pawn.color):
                    same.append([x, y])
        for i in range(len(same)):
            xs = same[i][0]
            ys = same[i][1]
            if (xs == x and ys == y):
                continue
            xn = xs - x
            yn = ys - y
            if (xs == x):
                y_min = same[i][1] if (same[i][1] < y) else y
                y_max = same[i][1] if (same[i][1] > y) else y
                for j in range(y_min+1, y_max-1):
                    remplace(x, j)
            if (ys == y):
                x_min = same[i][1] if (same[i][1] < x) else x
                x_max = same[i][1] if (same[i][1] > x) else x
                for j in range(x_min+1, x_max-1):
                    remplace(x, y)
            
    def replace(self, x, y):
        if (type(self.board[x][y]) == Pawn):
            self.board[x][y].changeColor()

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
