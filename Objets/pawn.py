class ColoursCodes:
    # this class contains colour codes to be used when printing in terminals
    GREEN = '\033[92m'
    RED = '\033[91m'

    # END ends colours and resets to default
    END = '\033[0m'


class Pawn:
    def __init__(self, color):
        self.available_color = [0, 1]
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        # to be safe, color can only be 0 and 1
        if color not in self.available_color:
            raise ValueError
        else:
            self.__color = color

    def change_color(self):
        # swaps the color
        if self.color == 1:
            self.color = 0
        else:
            self.color = 1

    def __str__(self):
        if self.color == 0:
            # colour codes affect all the text after being entered, so a stop code is needed
            return f'{ColoursCodes.GREEN}x{ColoursCodes.END}'
        else:
            return f'{ColoursCodes.RED}o{ColoursCodes.END}'
