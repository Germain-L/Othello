from .case import Case
from .pawn import Pawn

class Board:
    def __init__(self, size):

        self.__size = size
        self.__board = []
        self.__pawn_turn = Pawn(0)

        self.generate_board()

    @property
    def size(self) -> int:
        return self.__size

    @property
    def board(self):
        return self.__board

    @property
    def o_pawns(self) -> list:
        # reset list
        o_pawns = []

        # iterate over board
        for y in self.__board:
            for x in y:

                # if x contains a pawn and is of colour 1 then add it to the list
                if x.contains_pawn():
                    if x.pawn.color == 1:
                        o_pawns.append(x)

        return o_pawns

    @property
    def x_pawns(self) -> list:
        # reset list
        x_pawns = []

        # iterate over board
        for y in self.__board:
            for x in y:

                # if x contains a pawn and is of colour 0 then add it to the list
                if x.contains_pawn():
                    if x.pawn.color == 0:
                        x_pawns.append(x)

        return x_pawns

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
            self.__board.append(row)

    def check(self, x, y, pawn):
        reversed_pawns = []
        reversed_pawns.extend(self.check_around(0, +1, x, y, pawn))
        reversed_pawns.extend(self.check_around(0, -1, x, y, pawn))
        reversed_pawns.extend(self.check_around(+1, 0, x, y, pawn))
        reversed_pawns.extend(self.check_around(-1, 0, x, y, pawn))
        reversed_pawns.extend(self.check_around(-1, -1, x, y, pawn))
        reversed_pawns.extend(self.check_around(-1, +1, x, y, pawn))
        reversed_pawns.extend(self.check_around(+1, -1, x, y, pawn))
        reversed_pawns.extend(self.check_around(+1, +1, x, y, pawn))
        for pawn in reversed_pawns:
            self.replace(pawn[0], pawn[1])

    def check_around(self, param_x, param_y, func_x, func_y, pawn):
        same = []
        response = []
        x = func_x
        y = func_y

        # get all pawns with similar color like the placed pawn
        for i in range(len(self.__board)):
            x += param_x
            y += param_y

            # check if coordinates are out of bound
            if x < 0 or y < 0 or x >= len(self.__board) or y >= len(self.__board):
                break

            # check if case contains a pawn and if pawn's color is similar to placed pawn
            if self.__board[x][y].contains_pawn():
                if self.__board[x][y].pawn.color == pawn.color:
                    same.append([x, y])

        if len(same) > 0:
            for i in range(len(same)):
                x = same[i][0]
                y = same[i][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return response
                if not self.__board[x][y].contains_pawn():
                    return response
            for i in range(len(same)):
                x = same[i][0]
                y = same[i][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return response
                if self.__board[x][y].pawn.color != pawn.color:
                    response.append([x, y])
        return response

    def check_if_eat(self, x, y, pawn) -> bool:
        eated_pawns = []
        eated_pawns.extend(self.check_around(0, +1, x, y, pawn))
        eated_pawns.extend(self.check_around(0, -1, x, y, pawn))
        eated_pawns.extend(self.check_around(+1, 0, x, y, pawn))
        eated_pawns.extend(self.check_around(-1, 0, x, y, pawn))
        eated_pawns.extend(self.check_around(-1, -1, x, y, pawn))
        eated_pawns.extend(self.check_around(-1, +1, x, y, pawn))
        eated_pawns.extend(self.check_around(+1, -1, x, y, pawn))
        eated_pawns.extend(self.check_around(+1, +1, x, y, pawn))
        if (len(eated_pawns) > 0):
            return True
        else:
            return False

    def input_coord(self, available_coords) -> int:
        try:
            # try to enter a number and convert it to an int
            x = int(input(f"Enter x coordinate: ")) -1
            y = int(input(f"Enter y coordinate: ")) -1
            coord = [x, y]

            # check if entered coord fits in the board
            if coord not in available_coords:
                raise IndexError

            # return wiht -1 as list start at 0 and board start at 1
            return coord
        except ValueError:
            print(f"Please make sure to enter integer only, {coord_name} = {coord} is not an integer")

        except IndexError:
            print(f"{coord} is not valid, enter value in {available_coords}")

        # if we made it here then that means an error has occured
        # therefor we restart the function (recursion)
        return self.input_coord(available_coords)

    def get_available_coords(self, pawn):
        same_color_pawns = []
        available_coords = []
        for x in range(self.size):
            for y in range(self.size):
                if self.__board[x][y].contains_pawn():
                    if self.__board[x][y].pawn.color != pawn.color:
                        same_color_pawns.append([x, y])
        for same_color_pawn in same_color_pawns:
            possibilities = [[0, +1], [0, -1], [+1, 0], [-1, 0], [+1, +1], [-1, -1], [-1, +1], [+1, -1]]
            for coord in possibilities:
                x = same_color_pawn[0]+coord[0]
                y = same_color_pawn[1]+coord[1]
                if x > 0 or y > 0 or x <= len(self.__board) or y <= len(self.__board):
                    if not self.__board[x][y].contains_pawn():
                        if self.check_if_eat(x, y, pawn):
                            available_coords.append([x, y])
        return available_coords

    def new_pawn(self, pawn):
        self.__pawn_turn = pawn
        available_coord = self.get_available_coords(pawn)

        coord = self.input_coord(available_coord)

        if self.__board[coord[0]][coord[1]].contains_pawn():
            print("Pawn already exists here, try again")
            return self.new_pawn(pawn)
        # we have to swap x  and y,
        # because our board has rows and cols swapped
        self.place(coord[0], coord[1], pawn)

    def place(self, x, y, pawn):
        self.__board[x][y].pawn = pawn
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
                current_case = self.__board[x][y]

                # if x, y does not contain a pawn then board is not full
                if not current_case.contains_pawn():
                    full = False

        return full

    def __str__(self):
        str_board = " "

        nums = [n for n in range(1, self.size + 1)]

        available_coords = self.get_available_coords(self.__pawn_turn)

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
                if [x, y] in available_coords:
                    str_board += f'\033[40m•\033[0m '
                else:
                    str_board += f'{self.__board[x][y]} '

            # end line
            str_board += '\n'

        return str_board
