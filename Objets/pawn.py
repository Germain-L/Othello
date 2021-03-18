class Pawn:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def change_color(self):
        if self.color == 0:
            self.color = 1
        else:
            self.color = 0

    def __str__(self):
        if self.color == 0:
            return "o"
        return "x"