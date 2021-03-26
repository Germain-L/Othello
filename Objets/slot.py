class Slot:
    def __init__(self, x, y, size):
        self.__outer_bound = size
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        if x < 0 or x > self.__outer_bound:
            raise IndexError
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if y < 0 or y > self.__outer_bound:
            raise IndexError
        else:
            self.__y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'
