from random import choice

COLORS = "red blue green yellow brown purple".split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit > 0:
            self.limit -= 1
            return f"{choice(COLORS)} egg"
        else:
            raise StopIteration
