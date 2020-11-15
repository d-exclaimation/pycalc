"""
matrices.py
authored Vincent
"""


def main():
    """ Main function """
    first_matrix = Matrix([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1]
    ])

    second_matrix = Matrix([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1]
    ])
    print(first_matrix.inversed())
    print(first_matrix == second_matrix)


class Matrix:
    """ Matrix grid """

    def __init__(self, grid: list):
        """ Constructor """
        self.grid = grid
        columns = len(grid[0])
        for i in range(len(grid)):
            if len(grid[i]) != columns:
                raise TypeError
        self.size = [len(grid), len(grid[0])]

    def is_square(self):
        """ Check if matrix is a square """
        return self.size[0] == self.size[1]

    @staticmethod
    def identity(n: int) -> list:
        """ Get identity matrix """
        res = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            res.append(row)
        return res

    def __add__(self, other):
        """ Add two matrices """
        if type(other) != Matrix:
            raise TypeError
        if self.size[0] != other.size[0] or self.size[1] != other.size[1]:
            raise ValueError
        new_value = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(self.grid[i][j] + other.grid[i][j])
            new_value.append(row)
        return Matrix(new_value)

    def __sub__(self, other):
        """ Subtraction of matrices """
        if type(other) != Matrix:
            raise TypeError
        if self.size[0] != other.size[0] or self.size[1] != other.size[1]:
            raise ValueError
        new_value = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(self.grid[i][j] - other.grid[i][j])
            new_value.append(row)
        return Matrix(new_value)

    def __str__(self):
        """ String representative """
        new_value = ""
        for i in range(len(self.grid)):
            new_value += str(self.grid[i]) + "\n"
        return new_value

    def __eq__(self, other):
        """ Comparison with other """
        if type(other) != Matrix or self.size[0] != other.size[0] or self.size[1] != other.size[1]:
            return False
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True

    def tranpose(self):
        """ Transpose of self """
        if not self.is_square():
            raise ValueError
        new_grid = self.grid[:]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                new_grid[j][i] = self.grid[i][j]
        return Matrix(new_grid)

    def multiply(self, other: int):
        """ Multiply by Int """
        new_grid = self.grid[:]
        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                new_grid[i][j] *= other
        return Matrix(new_grid)

    def times(self, other):
        """ Multiply by matrix"""
        if type(other) != Matrix:
            raise TypeError
        if other.size[0] != self.size[1]:
            raise ValueError
        new_grid = []
        for i in range(0, self.size[0]):
            row = []
            for j in range(0, other.size[1]):
                column = []
                for x in range(len(self.grid[i])):
                    column.append(other.grid[x][j])
                row.append(Matrix.dot(self.grid[i], column))
            new_grid.append(row)
        return Matrix(new_grid)

    @staticmethod
    def dot(lhs: list, rhs: list) -> float:
        """ Dot product of two list """
        if len(lhs) != len(rhs):
            raise ValueError
        res = 0.0
        for i in range(len(lhs)):
            res += lhs[i] * rhs[i]
        return res

    def __mul__(self, other):
        """ Multiply by others """
        if type(other) == int:
            return self.multiply(other)
        if type(other) == Matrix:
            return self.times(other)
        raise TypeError

    def __reversed__(self):
        """ Inverted self """
        return self.inversed()

    def __pow__(self, power: int):
        """ Get power of matrix """
        if not self.is_square():
            raise ValueError
        new_value = Matrix(self.grid)
        for _ in range(1, power):
            new_value = (new_value * self)
        return new_value

    def inversed(self):
        """ Inversed of self """
        if not self.is_square():
            raise ValueError
        ide = Matrix.identity(self.size[0])

        new_grid = self.grid[:]
        for i in range(len(new_grid)):
            for j in range(i + 1, len(new_grid)):
                coef = new_grid[j][i] / new_grid[i][i]

                new_grid[j] = minus(new_grid[j], times(coef, new_grid[i]))
                ide[j] = minus(ide[j], times(coef, ide[i]))

        for x in range(len(new_grid)):
            rev = len(new_grid) - 1 - x
            for y in range(0, rev):
                coef = new_grid[y][rev] / new_grid[rev][rev]
                new_grid[y] = minus(new_grid[y], times(coef, new_grid[rev]))
                ide[y] = minus(ide[y], times(coef, ide[rev]))

        for p in range(len(new_grid)):
            if new_grid[p][p] < 0:
                new_grid[p] = times(-1, new_grid[p])
                ide[p] = times(-1, ide[p])
        return Matrix(ide)


def times(coef: float, array: list) -> list:
    """ Multiply a list by an float """
    return [(item * coef) for item in array]


def minus(lhs: list, rhs: list) -> list:
    """ reduce a list by another """
    return [lhs[i] - rhs[i] for i in range(len(lhs))]


if __name__ == '__main__':
    main()
