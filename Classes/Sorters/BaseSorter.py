


class BaseSorter:
    def __init__(self, dataset):
        self.dataset = dataset
        self.sorted = False
        self.print = True

    def add_dataset(self, dataset):
        self.dataset = dataset

    def show_dataset(self):
        if not self.print:
            return
        print(self.dataset)

    def _step(self):
        pass

    def sort(self, steps, pr = True):
        i = 0
        while not self.sorted:
            self._step()
            i += 1

            if i % steps == 0 and pr:
                i = 0
                self.show_dataset()

        return self.dataset

"""
jump bubble stooge 
"""