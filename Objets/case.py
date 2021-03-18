from .pawn import Pawn
from .pawn import Pawn

class Case:
    def __init__(self, pawn = None):
        self.__pawn = pawn

    @property
    def pawn(self):
        return self.__pawn

    @pawn.setter
    def pawn(self):
        self.__pawn = pawn

    def containsPawn(self):
        return False if self.__pawn == None else True
        
    def __str__(self):
        return "•" if self.__pawn == None else f'{self.__pawn}'