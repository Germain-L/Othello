class Pawn:
    def __init__(self, color):
        self.color = color

    def changeColor(self):
        if (self.color == 0):
            self.color == 1
        else:
            self.color == 0

    def view(self):
        return "o" if self.color == 0 else "x"

    def color(self):
        return self.color