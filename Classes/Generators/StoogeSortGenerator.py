from Classes.Generators.CasesClass import CasesClass

Cases = CasesClass()



class StoogeGen():
    def __init__(self):
        self.__size = 500
        self.__map = {
            Cases.worst: self.gen,
            Cases.average: self.gen,
            Cases.best: self.gen
        }

    def generate_table(self, case):
        sets = []
        curr_size = self.__size
        for q in range(0, 5):
            sets.append(self.__map[case](curr_size))
            curr_size *= 2

        return sets


    def gen(self, size):
        return [i for i in range(size)]
