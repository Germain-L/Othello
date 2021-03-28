from .case import Case
from .pawn import Pawn, ColoursCodes


class Board:
    def __init__(self, size):

        self.__size = size
        self.__board = []
        self.is_x_turn = True
        self.generate_board()
        print("")

    @property
    def size(self) -> int:
        return self.__size

    # -> list[list[Case]] is mostly used when writing the code as it helps with autocompletion
    @property
    def board(self):
        return self.__board

    @property
    def o_pawns(self) -> list:
        # reset list
        self.__o_pawns = []

        # iterate over board
        for y in range(self.size):
            for x in range(self.size):
                if self.__board[x][y].contains_pawn():
                    if self.__board[x][y].pawn.color == 1:
                        self.__o_pawns.append([x, y])

        return self.__o_pawns

    @property
    def x_pawns(self) -> list:
        # reset list
        self.__x_pawns = []

        # iterate over board
        for y in range(self.size):
            for x in range(self.size):
                if self.__board[x][y].contains_pawn():
                    if self.__board[x][y].pawn.color == 0:
                        self.__x_pawns.append([x, y])

        return self.__x_pawns

    @property
    def is_x_turn(self) -> bool:
        return self.__is_x_turn

    @is_x_turn.setter
    def is_x_turn(self, is_x_turn):
        self.__is_x_turn = is_x_turn

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

                elif y == mid + 1 and x == mid:
                    row[x].pawn = Pawn(1)

                elif y == mid and x == mid + 1:
                    row[x].pawn = Pawn(1)

                elif y == mid + 1 and x == mid + 1:
                    row[x].pawn = Pawn(0)

            # add the new row to the board
            self.__board.append(row)

    def check(self, func_x, func_y, pawn):
        reversed_pawns = []
        reversed_pawns.extend(self.check_around(0, +1, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(0, -1, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(+1, 0, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(-1, 0, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(-1, -1, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(-1, +1, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(+1, -1, func_x, func_y, pawn))
        reversed_pawns.extend(self.check_around(+1, +1, func_x, func_y, pawn))
        for pawn in reversed_pawns:
            self.replace(pawn[0], pawn[1])

    def check_around(self, param_x, param_y, func_x, func_y, pawn):
        same = []
        response = []
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
                    return response
                if not self.__board[x][y].contains_pawn():
                    return response
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return response
                if self.__board[x][y].pawn.color != pawn.color:
                    response.append([x, y])
        return response

    def verify_check_around(self, fake_board, param_x, param_y, func_x, func_y, pawn):
        same = []
        response = []
        x = func_x
        y = func_y
        for i in range(len(fake_board)):
            x += param_x
            y += param_y
            if x < 0 or y < 0 or x >= len(fake_board) or y >= len(fake_board):
                break
            if (fake_board[x][y].contains_pawn()
                    and fake_board[x][y].pawn.color == pawn.color):
                same.append([x, y])
        if len(same) > 0:
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return response
                if not fake_board[x][y].contains_pawn():
                    return response
            for j in range(len(same)):
                x = same[j][0]
                y = same[j][1]
                x -= param_x
                y -= param_y
                if x == func_x and y == func_y:
                    return response
                if fake_board[x][y].pawn.color != pawn.color:
                    response.append([x, y])
        return response

    def check_if_eat(self, board, func_x, func_y, pawn) -> bool:
        eaten_pawns = []
        eaten_pawns.extend(self.verify_check_around(board, 0, +1, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, 0, -1, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, +1, 0, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, -1, 0, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, -1, -1, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, -1, +1, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, +1, -1, func_x, func_y, pawn))
        eaten_pawns.extend(self.verify_check_around(board, +1, +1, func_x, func_y, pawn))
        if len(eaten_pawns) > 0:
            return False
        else:
            return True

    def make_fake_board(self, x, y, pawn):
        # copy current board
        fake_board = self.__board

        # add pawn that we want to test with
        fake_board[x][y].pawn = pawn

        # return fake board with test pawn
        return fake_board

    def get_availble_plays_around_colour(self, color):
        # this represent a list of available coords that the player can play
        available_plays = []

        case_list = []

        if color == 0:
            case_list = self.x_pawns
        elif color == 1:
            case_list = self.o_pawns

        for case in case_list:
            # this list represents all the cases around the pawn
            around_current_case = []

            # iterate over 3 cases (case.x + 2 is outside the range so it stops at case.x + 1)
            for x in range(case[0] - 1, case[0] + 2):
                if x < 0 or x > self.size:
                    continue

                # iterate over 3 cases (case.y + 2 is outside the range so it stops at case.y + 1)
                for y in range(case[1] - 1, case[1] + 2):
                    if y < 0 or y > self.size:
                        continue

                    # we don't add pawn we're currently looking at
                    if x != case[0] and y != case[1]:
                        around_current_case.append([x, y])

            # iterate over possible plays, to check if they eat opponent's pawns
            for possible_play in around_current_case:
                fake_pawn = Pawn(color)
                x, y = possible_play[0], possible_play[1]
                fake_board = self.make_fake_board(x, y, fake_pawn)
                # if possible_play eats opponent's pawn then we add it to the list of plays the player can do

                if self.check_if_eat(fake_board, x, y, fake_pawn):
                    print(f"can play {possible_play}")
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

        # create number line on top row for columns
        for n in nums:
            str_board += f" {n}"

        # end line
        str_board += '\n'

        available_plays_x = self.get_availble_plays_around_colour(0)
        available_plays_o = self.get_availble_plays_around_colour(1)

        # available_plays_x = [[2, 4], [3, 5], [4, 2], [5, 3]]
        # available_plays_o = [[2, 3], [3, 2], [4, 5], [5, 4]]

        # iterate over each row
        for y in range(self.size):

            # add row number
            str_board += f"{nums[y]} "

            # iterate of each case
            for x in range(self.size):

                # add each case to the string
                if self.is_x_turn:
                    if [x, y] in available_plays_x:
                        str_board += f'{ColoursCodes.PURPLE}{self.board[x][y]}{ColoursCodes.END} '
                        # str_board += f'✓ '
                    else:
                        str_board += f'{self.board[x][y]} '
                else:
                    if [x, y] in available_plays_o:
                        str_board += f'{ColoursCodes.PURPLE}{self.board[x][y]}{ColoursCodes.END} '
                    else:
                        str_board += f'{self.board[x][y]} '
            # end line
            str_board += '\n'

        return str_board
