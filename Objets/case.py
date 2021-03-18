from .pawn import Pawn
from .pawn import Pawn


class Case:
    def __init__(self, pawn = None):
        self.__pawn = pawn

    @property
    def pawn(self):
        return self.__pawn

    @pawn.setter
    def pawn(self, value):
        self.__pawn = value

    def contains_pawn(self):
        if self.pawn is None:
            return False

        return True

    def __str__(self):
        if self.contains_pawn():
            return f'{self.__pawn}'

        return "•"
