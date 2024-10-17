from random import randint

from Classes.Generators.CasesClass import  CasesClass

Cases = CasesClass()

class BubbleGen():
    def __init__(self):
        self.__size = 500
        self.__map = {
            Cases.worst : self.worst,
            Cases.average : self.avg,
            Cases.best : self.best
        }

    def generate_table(self, case):
        sets = []
        curr_size = self.__size
        for q in range(0, 5):
            sets.append(self.__map[case](size = curr_size))
            curr_size *= 2

        return sets

    def best(self, size):
        _set = []
        for i in range(0, size):
            _set.append(i)
        return _set


    def worst(self, size):
        _set = []
        for i in range (0, size):
            _set.append(randint(0, 1000))
        return _set

    def avg(self, size):
        _set = []
        for i in range(size, 0, -1):
            _set.append(i)
        return  _set
