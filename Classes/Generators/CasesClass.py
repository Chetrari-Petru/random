class CasesClass:
    def __init__(self):
        self.worst = 0
        self.average = 1
        self.best = 2

    def __eq__(self, other):
        for k, v in vars(self):
            if v == other:
                return True
        return False
