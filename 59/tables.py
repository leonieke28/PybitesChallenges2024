class MultiplicationTable:
    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
        their calculations (form of caching)"""
        self._table = [
            [x * y for x in range(1, length + 1)] for y in range(1, length + 1)
        ]

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) ** 2

    def __str__(self):
        """Returns a string representation of the table"""
        return "\n".join([" | ".join(map(str, row)) for row in self._table])

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x < 1 or x > len(self._table) or y < 1 or y > len(self._table):
            raise IndexError("x and y coordinates must be within the table boundaries")
        return self._table[x - 1][y - 1]
