from random import randint
from Classes.JumpSearch import JumpSearch
from Classes.Sorters.BubbleSort import BubbleSort
from Classes.Sorters.Stooge3 import stoogesort
from Classes.Generators.CasesClass import CasesClass
from Classes.Generators.TableGenerator import TableGenerator
from timeit import  default_timer as timer
from prettytable import PrettyTable

Cases = CasesClass()


class Menu:
    def __init__(self):
        self.running = True
        self.dataset = []
        self.run_dataset = []
        self.__generator = TableGenerator()


        self.options = {
            "1" : {"text" : "Generate dataset", "func" : self.__generate_dataset},
            "2" : {"text" : "Search in dataset", "func" : self.__search},
            "3" : {"text" : "Bubble Sort", "func" : self.__bubble},
            "4" : {"text" : "Stooge Sort", "func" : self.__stooge},

            "5" : {"text" : "Test for best case", "func" : self.__best},
            "6" : {"text" : "Test for average case", "func" : self.__avg},
            "7" : {"text" : "Test for worst case", "func" : self.__worst},
            " " : {"text" : "", "func" : None},
            "0" : {"text" : "Exit", "func" : self.__exit},
        }


    def __print_menu(self):
        print("----------------------")
        print("MENU")
        for key in self.options:
            print("{0}  {1}".format(key, self.options[key]["text"]))
        print("----------------------")
        print("dataset: {0}".format(self.dataset))
        print("----------------------")

    def __verify_input_int(self, message):
        while True :
            try:
                return int(input(message))
            except:
                print("Please input a integer")

    def __generate_dataset(self):
        size = self.__verify_input_int("Choose the size of the set: ")

        dataset = []

        for i in range(0, size):
            dataset.append(randint(0, 1000))

        print(dataset)
        self.dataset = dataset
        self.run_dataset = dataset

    def __search(self):
        needle = self.__verify_input_int("Element to search: ")
        steps = None
        while not steps:
            steps = self.__verify_input_int("Steps: ")

            if steps < 1:
                print("Steps must be more than 0")
                steps = None
            if steps >= len(self.dataset):
                print("Steps must be less than size of set")
                steps = None


        data_clone = self.run_dataset.copy()
        found = JumpSearch(data_clone).search(needle, steps)
        if found == -1:
            print("Please sort the array before searching")
        elif found:
            print("{0} does belong to the set".format(needle))
        else:
            print("{0} does not belong to the set".format(needle))

    def __bubble(self):
        steps = self.__verify_input_int("Steps: ")
        data_clone = self.dataset.copy()
        data = BubbleSort(data_clone).sort(steps)
        print(data)
        self.run_dataset = data_clone

    def __stooge(self):
        steps = self.__verify_input_int("Steps: ")
        print(steps)
        data_clone = self.dataset.copy()
        stoogesort(data_clone,0,len(self.dataset) - 1, 1, steps)
        print(data_clone)
        self.run_dataset = data_clone

    def __run_test(self, case):
        tables = self.__generator.generate_table(case)

        statistics = {
            "stooge" : [],
            "bubble" : []
        }
        for gen in tables:
            for _set in tables[gen]:
                print("running {0} sort on {1} elements set".format(gen, len(_set)))
                if gen == "bubble":

                    sorter = BubbleSort(_set)
                    tick = timer()
                    sorter.sort(1, False)

                    end = timer()
                    statistics[gen].append(end-tick)
                else:
                    tick = timer()
                    stoogesort(_set, 0, len(_set)-1,1,1, False)
                    end=  timer()
                    statistics[gen].append(end-tick)

        CompTable = PrettyTable()
        names = ["Size of set"]
        names.append(gen for gen in self.__generator.generators)

        CompTable.fields_names = names
        CompTable.add_column(names[0], [500, 1000, 2000, 4000, 8000])
        CompTable.add_column(names[1], statistics["bubble"])
        CompTable.add_column(names[2], statistics["stooge"])

        # print(CompTable)

    def __best(self):
        self.__run_test(Cases.best)

    def __avg(self):
        self.__run_test(Cases.average)

    def __worst(self):
        self.__run_test(Cases.worst)

    def __exit(self):
        self.running = False

    def run_menu(self):
        while self.running:
            self.__print_menu()
            option = input("Choose an option: ")

            try:

                self.options[option]["func"]()
            except InterruptedError:
                print("Please choose a valid option")


Menu().run_menu()