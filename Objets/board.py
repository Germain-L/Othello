from .pawn import Pawn
from .case import Case
from .slot import Slot


class Board:
    def __init__(self, size):
        self.size = size
        self.generate()
        self.start()

        self.__white = []
        self.__black = []

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def black(self) -> list:
        return self.__black

    @property
    def whites(self) -> list:
        return self.__white

    def add_black(self, slot):
        self.black.append(slot)

    def add_white(self, slot):
        self.whites.append(slot)

    def generate(self):
        # TODO DELETE
        self.__board = [[Case()] * self.size for _ in range(self.size)]

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
                if type(self.__board[x][y]) == Pawn:
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
        self.__board[x][y] = Case(pawn)
        self.check(x, y, pawn)

    def check(self, func_x, func_y, pawn):
        same = []
        for x in range(len(self.__board)):
            for y in range(len(self.__board)):
                if (self.__board[x][y].contains_pawn()
                        and self.__board[x][y].pawn.color == pawn.color):
                    same.append([x, y])
        for i in range(len(same)):
            xs = same[i][0]
            ys = same[i][1]
            if xs == func_x and ys == func_y:
                continue
            # FACTOR
            if xs == func_x:
                y_min = ys if (ys < func_y) else func_y
                y_max = ys if (ys > func_y) else func_y
                for j in range(y_min + 1, y_max):
                    if not self.__board[xs][j].contains_pawn():
                        return
                for j in range(y_min + 1, y_max):
                    if self.__board[xs][j].pawn.color != pawn.color:
                        self.replace(xs, j)
            if ys == func_y:
                x_min = xs if (xs < func_x) else func_x
                x_max = xs if (xs > func_x) else func_x
                for j in range(x_min + 1, x_max):
                    if not self.__board[j][ys].contains_pawn():
                        return
                for j in range(x_min + 1, x_max):
                    if self.__board[j][ys].pawn.color != pawn.color:
                        self.replace(j, ys)
            ##
            if ys != func_y and xs != func_x:
                self.check_around(-1, -1, func_x, func_y, pawn)
                self.check_around(-1, +1, func_x, func_y, pawn)
                self.check_around(+1, -1, func_x, func_y, pawn)
                self.check_around(+1, +1, func_x, func_y, pawn)

    def check_around(self, param_x, param_y, func_x, func_y, pawn):
        same = []
        x = func_x
        y = func_y
        for i in range(len(self.__board)):
            x += param_x
            y += param_y
            if x < 0 or y < 0 or x >= len(self.__board) or y >= len(self.__board):
                break
            if (self.__board[x][y].contains_pawn()
                    and self.__board[x][y].pawn.color == pawn.color):
                same.append([x, y])
        if len(same) > 0:
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return
                if not self.__board[x][y].contains_pawn():
                    return
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return
                if self.__board[x][y].pawn.color != pawn.color:
                    self.replace(x, y)

    def check_available_germain(self, param_x, param_y, func_x, func_y, pawn):
        same = []
        x = func_x
        y = func_y
        for i in range(len(self.__board)):
            x += param_x
            y += param_y
            if x < 0 or y < 0 or x >= len(self.__board) or y >= len(self.__board):
                break
            if (self.__board[x][y].contains_pawn()
                    and self.__board[x][y].pawn.color == pawn.color):
                same.append([x, y])
        if len(same) > 0:
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return
                if not self.__board[x][y].contains_pawn():
                    return
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return
                if self.__board[x][y].pawn.color != pawn.color:
                    self.replace(x, y)


    def replace(self, x, y):
        if self.__board[x][y].contains_pawn():
            self.__board[x][y].pawn.change_color()

    def new_pawn(self, pawn):
        """Lets the user input coordinates to place a pawn"""
        if pawn.color == 0:
            for i in self.whites:
                self.check_if_available(i)


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

        while self.__board[x][y].contains_pawn():
            print("Invalid coordinates pawn already present")
            y = int(input('enter x coordinate for new pawn: '))
            x = int(input('enter y coordinate for new pawn: '))

            try:
                x = int(x) - 1
                y = int(y) - 1

                if x not in allowed or y not in allowed:
                    print(f"Please make sure to enter numbers between 1 and {self.size}")

            except ValueError:
                print(f"Please make sure to enter numbers only")

        self.place(x, y, pawn)

        if pawn.color == 0:
            self.add_white(Slot(x, y, self.size))
        elif pawn.color == 1:
            self.add_black(Slot(x, y, self.size))

        print(f"Added pawn in {x}, {y}")

    def check_if_available(self, slot):
        x = slot.x
        y = slot.y
        around = []
        try:
            tl = Slot(x-1, y-1, self.size)
            ts = Slot(x, y-1, self.size)
            tr = Slot(x+1, y - 1, self.size)

            l = Slot(x-1, y, self.size)
            r = Slot(x+1, y, self.size)

            bl = Slot(x-1, y+1, self.size)
            bs = Slot(x, y+1, self.size)
            br = (x+1, y+1, self.size)

        except IndexError:
            print("Pion au bord")
        for slot in around:
            print(slot)

    def check_full(self):
        for x in range(len(self.__board)):
            for y in range(len(self.__board)):
                if not self.__board[x][y].contains_pawn:
                    return True
        return False

    def check_end(self):
        contains_white = False
        contains_black = False

        white_count = 0
        black_count = 0

        full = self.check_full()

        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                if self.__board[x][y].contains_pawn():
                    if self.__board[x][y].pawn.color == 0:
                        white_count += 1
                        contains_white = True
                    else:
                        black_count += 1
                        contains_black = True
        if contains_white and not contains_black:
            print("Blanc gagne")
            return True

        elif contains_black and not contains_white:
            print("Noir gagne")
            return True

        elif full:
            if white_count > black_count:
                print("Blanc gagne")
                return True

            elif black_count > white_count:
                print("Noir gagne")
                return True

            else:
                print("Execo")
                return True
        return False
