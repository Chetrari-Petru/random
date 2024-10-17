from Classes.Sorters.BaseSorter import BaseSorter

class StoogeSort(BaseSorter):
    def __init__(self, dataset, current_step = 0):
        super().__init__(dataset)
        self.current_step = current_step

    def _step(self, steps, start, end):
        if start > end:
            return

        if self.dataset[start] > self.dataset[end]:
            c = self.dataset[start]
            self.dataset[start] = self.dataset[end]
            self.dataset[end] = c


        if end - start + 1 > 2:
            one_third = (end - start +1)//3

            self.dataset = StoogeSort(self.dataset, self.current_step).sort(steps, start=start, end=end - one_third)
            self.dataset = StoogeSort(self.dataset, self.current_step).sort(steps, start=one_third, end=end)
            self.dataset = StoogeSort(self.dataset, self.current_step).sort(steps, start=start, end=end - one_third)

        return self.dataset

    def sort(self, steps, start, end):
        i = 0
        while not self.sorted:
            self.dataset = self._step(steps, start, end)
            i += 1

            if i % steps == 0:
                i = 0
                self.show_dataset()

        return self.dataset



