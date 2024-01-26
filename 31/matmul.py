class Matrix:
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        result = [
            [0 for _ in range(len(other.values[0]))] for _ in range(len(self.values))
        ]
        for i in range(len(self.values)):
            for j in range(len(other.values[0])):
                for k in range(len(other.values)):
                    result[i][j] += self.values[i][k] * other.values[k][j]
        return Matrix(result)

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __imatmul__(self, other):
        result = self.__matmul__(other)
        self.values = result.values
        return self
