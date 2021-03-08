class Pawn:
    def __init__(self, color):
        self.color = color

    def changeColor(self):
        #TODO reverse color
        pass

    def view(self):
        return "o" if self.color == 0 else "x"