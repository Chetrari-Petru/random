from Classes.Sorters.BaseSorter import BaseSorter

class StoogeSort (BaseSorter):
    def __init__(self, dataset, current_step = 0):
        super().__init__(dataset)
        self.current_step = current_step

    def __cut_dataset(self, start, end):
        if start < 0 or start > end or end > len(self.dataset)-1:
            raise IndexError
        i = start
        new_dataset = []
        while i <= end:
            new_dataset.append(self.dataset[i])
            i+=1

        return new_dataset

    def __modify_dataset_segment(self, start, end, modified_segment):
        if start < 0 or start > end or end > len(self.dataset):
            raise IndexError

        new_dataset = []
        i=0
        while i < len(self.dataset):
            if i < start or i > end:
                new_dataset.append(self.dataset)
            else:
                new_dataset.append(modified_segment[i - start])

    def _step(self, start, end):
        if start>=end:
            return

        # sort algorithm gives a segment of the dataset
        # because you can't really pass by reference in python
        # so you cut the dataset, sort it, cut it more, yada yada
        # and then you put it back together piece by piece
        # (you could use indexes ...
        # ...
        # not fun)


        # sort the first 2 thirds
        self.current_step += 1
        modified_segment, self.current_step = StoogeSort(self.__cut_dataset(start, end), self.current_step).sort(1)
        self.dataset = self.__modify_dataset_segment(start, end, modified_segment)




    def sort(self, steps):
        first, last = 0, len(self.dataset) - 1
        if last < 2:
            return self.dataset, self.current_step


        if self.dataset[first] > self.dataset[last]:
            c = self.dataset[first]
            self.dataset[first] = self.dataset[last]
            self.dataset[last] = c

        third = (last + 1) // 3

        self._step(0, last-third)
        if self.current_step % steps == 0:
            self.show_dataset()

        self._step(third, last)
        if self.current_step % steps == 0:
            self.show_dataset()

        self._step(0, last-third)
        if self.current_step % steps == 0:
            self.show_dataset()

        return self.dataset, self.current_step
