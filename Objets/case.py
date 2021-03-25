from .pawn import Pawn

class Case:
    def __init__(self, pawn=None):
        self.__pawn = pawn

    @property
    def pawn(self):
        return self.__pawn

    @pawn.setter
    def pawn(self, pawn):
        self.__pawn = pawn

    def contains_pawn(self):
        if self.pawn is None:
            return False
        return True

    def __str__(self):
        if self.contains_pawn():
            return f'{self.__pawn}'

        return "•"
