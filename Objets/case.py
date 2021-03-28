from .pawn import Pawn


class Case:
    def __init__(self, x, y, pawn=None):
        self.__x = x
        self.__y = y
        self.__pawn = pawn

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def pawn(self) -> Pawn:
        return self.__pawn

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @pawn.setter
    def pawn(self, pawn):
        self.__pawn = pawn

    def contains_pawn(self) -> bool:
        """Boolean value whether the case holds a pawn or not"""
        if self.pawn is None:
            return False
        return True

    def __str__(self):
        # if case has pawns then returns __str__ function of pawn
        if self.contains_pawn():
            return f'{self.pawn}'

        # or empty case which is represented by this
        return '•'
