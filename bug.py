import option
import random


class Bug:
    def __init__(self, points):
        self.__point = None
        self.quickly_move(points)

    @property
    def point(self):
        return [self.__point]

    def quickly_move(self, points: list):
        while True:
            row = random.randint(1, option.size - 3)
            col = random.randint(1, option.size - 3)
            if (row, col) not in points:
                break
        self.__point = (row, col)
