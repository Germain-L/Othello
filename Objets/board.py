from .pawn import Pawn


class Board:
    def __init__(self, size):
        self.size = size
        self.generate()
        self.start()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def generate(self):
        # TODO DELETE
        self.__board = [["•"] * self.size for _ in range(self.size)]

    def __str__(self):
        """Displays the board in a grid"""
        board = ""

        nums = [i for i in range(1, self.size + 1)]

        board += " "

        for i in nums:
            board += f' {i}'

        board += "\n"

        for x in range(len(self.__board)):
            board += f'{nums[x]} '
            for y in range(len(self.__board[x])):
                if (type(self.__board[x][y]) == Pawn):
                    board += f'{self.__board[x][y]} '
                else:
                    board += f'{self.__board[x][y]} '
            board += "\n"

        return board

    def start(self):
        x = (self.size // 2) - 1
        y = (self.size // 2) - 1
        self.place(x, y, Pawn(0))
        self.place(x + 1, y, Pawn(1))
        self.place(x, y + 1, Pawn(1))
        self.place(x + 1, y + 1, Pawn(0))

    def place(self, x, y, pawn):
        self.__board[x][y] = pawn
        self.check(x, y, pawn)
    
    def check(self, func_x, func_y, pawn):
        same = []
        for x in range(len(self.__board)):
            for y in range(len(self.__board)):
                if (type(self.__board[x][y]) == Pawn
                and self.__board[x][y].color == pawn.color):
                    same.append([x, y])
        for i in range(len(same)):
            xs = same[i][0]
            ys = same[i][1]
            if (xs == func_x and ys == func_y):
                continue
            # FACTOR
            if (xs == func_x):
                y_min = ys if (ys < func_y) else func_y
                y_max = ys if (ys > func_y) else func_y
                for j in range(y_min+1, y_max):
                    self.replace(xs, j)
            if (ys == func_y):
                x_min = xs if (xs < func_x) else func_x
                x_max = xs if (xs > func_x) else func_x
                for j in range(x_min+1, x_max):
                    self.replace(j, ys)
            ##
            if (ys != func_y and xs != func_x):
                self.checkDiag(-1, -1, pawn)
                self.checkDiag(-1, +1, pawn)
                self.checkDiag(+1, -1, pawn)
                self.checkDiag(+1, +1, pawn)

    def checkDiag(self, paramX, paramY, pawn):
        x = 0
        y = 0
        same = []
        for i in range(len(self.board)):
            if (type(self.board[x][y]) == Pawn 
            and self.board[x][y].color == pawn.color):
                same.append([x, y])
            x += paramX
            y += paramY
        # self.checkSame(same, x, y)
    
    # def checkSame(self, same, x, y):
    #     x_min = same[i][0] if (same[i][0] < x) else x
    #     x_max = same[i][0] if (same[i][0] > x) else x
    #     y_min = same[i][1] if (same[i][1] < y) else y
    #     y_max = same[i][1] if (same[i][1] > y) else y
    #     for i in range(x_min+1, x_max):
    #         for j in range(y_min+1, y_max):
    #             self.replace(i, j)

            
    def replace(self, x, y):
        if (type(self.__board[x][y]) == Pawn):
            self.__board[x][y].changeColor()

    def isEmpty(self, x, y):
        return False if (type(self.__board[x][y]) == Pawn) else True

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

        while not self.isEmpty(x, y):
            print("Invalid coordinates pawn already present")
            y = input('enter x coordinate for new pawn: ')
            x = input('enter y coordinate for new pawn: ')

        self.place(x, y, pawn)
        print(f"Added pawn in {x}, {y}")

    def check_end(self):
        contains_white = False
        contains_black = False

        white_count = 0
        black_count = 0

        full = True

        for x in range(len(self.__board)):
            if "•" in self.__board[x]:
                full = False
            for y in range(len(self.__board[x])):
                current_pawn = self.__board[x][y]
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
