from Classes.Generators.CasesClass import CasesClass
from Classes.Generators.BubbleSortGenerator import BubbleGen
from Classes.Generators.StoogeSortGenerator import StoogeGen

Cases = CasesClass() # Enums

class TableGenerator:
    def __init__(self):
        self.generators = {
            "bubble": BubbleGen(),
            "stooge": StoogeGen()
        }

    def generate_table(self, case):
        sets = {
            "bubble" : None,
            "stooge" : None
        }
        for generator in self.generators:
            sets[generator] = self.generators[generator].generate_table(case)

        return sets
