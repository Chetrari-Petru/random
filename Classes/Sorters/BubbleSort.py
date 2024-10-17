from Classes.Sorters.BaseSorter import BaseSorter

class BubbleSort (BaseSorter):
    def __init__(self, dataset):
        super().__init__(dataset)

    def _step(self):
        swapped = False
        for i in range(0,len(self.dataset)-1):
            if self.dataset[i] > self.dataset[i+1]:
                c = self.dataset[i]
                self.dataset[i] = self.dataset[i+1]
                self.dataset[i + 1] = c
                swapped = True

        self.sorted = not swapped