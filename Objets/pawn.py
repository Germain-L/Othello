class Pawn:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def changeColor(self):
        if self.color == 0:
            self.color = 1
        else:
            self.color = 0

    def __str__(self):
        return "o" if self.color == 0 else "x"