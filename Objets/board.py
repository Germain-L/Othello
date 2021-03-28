from .case import Case
from .pawn import Pawn


class Board:
    def __init__(self, size):

        self.__size = size
        self.__board = []

        self.generate_board()

    @property
    def size(self) -> int:
        return self.__size

    # -> list[list[Case]] is mostly used when writing the code as it helps with autocompletion
    @property
    def board(self) -> list[list[Case]]:
        return self.__board

    @property
    def o_pawns(self) -> list:
        # reset list
        self.__o_pawns = []

        # iterate over board
        for y in self.board:
            for x in y:

                # if x contains a pawn and is of colour 1 then add it to the list
                if x.contains_pawn():
                    if x.pawn.color == 1:
                        self.__o_pawns.append(x)

        return self.__o_pawns

    @property
    def x_pawns(self) -> list:
        # reset list
        self.__x_pawns = []

        # iterate over board
        for y in self.board:
            for x in y:

                # if x contains a pawn and is of colour 0 then add it to the list
                if x.contains_pawn():
                    if x.pawn.color == 0:
                        self.__x_pawns.append(x)

        return self.__x_pawns

    def generate_board(self):
        # get middle of the board, -1 because index starts at 0
        mid = self.size // 2 - 1

        # create rows
        for y in range(self.size):

            # instatiate an empty row to be filled in
            row = []

            # create collumns
            for x in range(self.size):

                # add a new Case with x and y coordinates
                row.append(Case(x, y))

                # place pawns in the middle of the board at the start of the game
                if y == mid and x == mid:

                    # place a pawn on the newly created Case
                    row[x].pawn = Pawn(0)
                    self.x_pawns.append(row[x])

                elif y == mid + 1 and x == mid:
                    row[x].pawn = Pawn(1)
                    self.o_pawns.append(row[x])

                elif y == mid and x == mid + 1:
                    row[x].pawn = Pawn(1)
                    self.o_pawns.append(row[x])

                elif y == mid + 1 and x == mid + 1:
                    row[x].pawn = Pawn(0)
                    self.x_pawns.append(row[x])

            # add the new row to the board
            self.board.append(row)

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

    def check_if_eat(self, x, y) -> bool:
        eats = False

        # change eats to true if a pawn gets eaten if the player plays this x, y

        return eats

    def get_availble_plays_around_pawn(self, color):
        # this represent a list of available coords that the player can play
        available_plays = []

        for case in self.x_pawns:

            # this list represents all the cases around the pawn
            around_current_case = []

            # iterate over 3 cases (case.x + 2 is outside the range so it stops at case.x + 1)
            for x in range(case.x - 1, case.x + 2):
                if x < 0 or x > self.size:
                    continue

                # iterate over 3 cases (case.y + 2 is outside the range so it stops at case.y + 1)
                for y in range(case.y - 1, case.y + 2):
                    if y < 0 or y > self.size:
                        continue

                    # we don't add pawn we're currently looking at
                    if x != case.x and y != case.y:
                        around_current_case.append(self.board[x][y])

            # iterate over possible plays, to check if they eat opponent's pawns
            for possible_play in around_current_case:

                # if possible_play eats opponent's pawn then we add it to the list of plays the player can do
                if self.check_if_eat(possible_play.x, possible_play.y):
                    available_plays.append(possible_play)

            return available_plays

    def input_single_coord(self, coord_name, available_coords) -> int:
        coord = ""

        try:
            # try to enter a number and convert it to an int
            coord = int(input(f"Enter {coord_name} coordinate: "))

            # check if entered coord fits in the board
            if coord not in available_coords:
                raise IndexError

            # return wiht -1 as list start at 0 and board start at 1
            return coord - 1
        except ValueError:
            print(f"Please make sure to enter integer only, {coord_name} = {coord} is not an integer")

        except IndexError:
            print(f"{coord} is not valid, enter value in {available_coords}")

        # if we made it here then that means an error has occured
        # therefor we restart the function (recursion)
        return self.input_single_coord(coord_name, available_coords)

    def new_pawn(self, pawn):
        available_coord = [n for n in range(1, self.size + 1)]

        x = self.input_single_coord("x", available_coord)
        y = self.input_single_coord("y", available_coord)

        if self.__board[x][y].contains_pawn():
            print("Pawn already exists here, try again")
            return self.new_pawn(pawn)
        # we have to swap x  and y,
        # because our board has rows and cols swapped
        self.place(x, y, pawn)

    def place(self, x, y, pawn):
        self.board[x][y].pawn = pawn
        self.check(x, y, pawn)

    def replace(self, x, y):
        # check if board contains pawn, otherwise, will raise an Error
        if self.__board[x][y].contains_pawn():
            self.__board[x][y].pawn.change_color()

    def game_ended(self) -> bool:
        # if the board is full then end the game
        full = True

        # iterate over the board
        for y in range(self.size):
            for x in range(self.size):

                # get case at x, y
                current_case = self.board[x][y]

                # if x, y does not contain a pawn then board is not full
                if not current_case.contains_pawn():
                    full = False

        return full

    def __str__(self):
        str_board = " "

        nums = [n for n in range(1, self.size + 1)]

        # create number line on top row for columns
        for n in nums:
            str_board += f" {n}"

        # end line
        str_board += '\n'

        # iterate over each row
        for y in range(self.size):

            # add row number
            str_board += f"{nums[y]} "

            # iterate of each case
            for x in range(self.size):
                # add each case to the string
                str_board += f'{self.board[x][y]} '

            # end line
            str_board += '\n'

        return str_board
