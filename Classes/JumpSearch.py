class JumpSearch:
    def __init__(self, dataset):
        self.dataset = dataset

    def _check_sorted(self):
        for i in range(0, len(self.dataset)-2):
            if(self.dataset[i] > self.dataset[i+1]):
                return False
        return True

    def search(self, needle, steps):
        if not self._check_sorted():
            return -1


        i = 0
        cont = True
        while cont:
            out = False
            if i >= len(self.dataset):
                out = True
                i -= steps
            if self.dataset[i] == needle:
                return True

            if self.dataset[i] < needle and not out:
                i += steps
            else:
                base = i
                i -= steps
                while i <= base:
                    if self.dataset[i] == needle:
                        return True
                    i+=1
                return False
        return False


