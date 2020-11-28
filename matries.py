"""
matrices.py
authored Vincent
authored by Vincent
version 1.0.2
last modified Nov 28, 2020 at 3:59 PM (UTC + 7)
Copyright © 2020 Vincent. All rights reserved.
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

        # Validate column size
        for row in grid:
            if len(row) != columns:
                raise TypeError("Not a valid Matrix with defined size of n x m")
        self.size = [len(grid), len(grid[0])]

    def is_square(self):
        """ Check if matrix is a square """
        return self.size[0] == self.size[1]

    @staticmethod
    def identity(num: int) -> list:
        """ Get identity matrix """

        # Create a zero matrix grid, but diagonal are 1s
        res = []
        for i in range(num):
            row = []
            for j in range(num):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            res.append(row)
        return res

    def __add__(self, other):
        """ Add two matrices """

        # Validate type and value given: same size and same type
        if not isinstance(other, Matrix):
            raise TypeError("Cannot operate with a non Matrix")
        if self.size[0] != other.size[0] or self.size[1] != other.size[1]:
            raise ValueError("Cannot do operation with the given sizes for the matrices")
            
        # Create a new value by adding all items in the grid
        new_value = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(self.grid[i][j] + other.grid[i][j])
            new_value.append(row)
        return Matrix(new_value)

    def __sub__(self, other):
        """ Subtraction of matrices """

        # Validate type and value given: same size and same type
        if not isinstance(other, Matrix):
            raise TypeError("Cannot operate with a non Matrix")
        if self.size[0] != other.size[0] or self.size[1] != other.size[1]:
            raise ValueError("Cannot do operation with the given sizes for the matrices")

        # Create a new value by subtracting all items in the grid
        new_value = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                row.append(self.grid[i][j] - other.grid[i][j])
            new_value.append(row)
        return Matrix(new_value)

    def __str__(self):
        """ String representative, in 2D """
        new_value = ""
        for i in range(len(self.grid)):
            new_value += str(self.grid[i]) + "\n"
        return new_value

    def __eq__(self, other):
        """ Comparison with other """

        # Check for type and size
        same_size = self.size[0] != other.size[0] or self.size[1] != other.size[1]
        if not isinstance(other, Matrix) or same_size:
            return False
        
        # Check for each item in grids
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True

    def transpose(self):
        """ Transpose of self """
        if not self.is_square():
            raise ValueError("Cannot do operation with the given sizes for the matrices")

        # The new grid will just the original but the element has its indexes switch
        new_grid = [
            [self.grid[j][i] for j in range(len(self.grid[i]))] for i in range(len(self.grid))
        ]
        return Matrix(new_grid)

    def multiply(self, other: int):
        """ Multiply by Int """
        new_grid = self.grid[:]

        # For each item in the grid, multiply it by the parameter
        for i, row in enumerate(new_grid):
            for j in range(len(row)):
                new_grid[i][j] *= other
        return Matrix(new_grid)

    def times(self, other):
        """ Multiply by matrix"""

        # Validate type and value given: valid size and same type
        if not isinstance(other, Matrix):
            raise TypeError("Cannot operate with a non Matrix")
        if other.size[0] != self.size[1]:
            raise ValueError("Cannot do operation with the given sizes for the matrices")

        # Create an empty grid to fill in
        new_grid = []

        # Loop through each row in self, and loop through for each column in other
        for i in range(0, self.size[0]):
            row = []
            for j in range(0, other.size[1]):

                # create a array of column j from other
                column = []
                for k in range(len(self.grid[i])):
                    column.append(other.grid[k][j])
                
                # For row i and column j should be the dot product
                # of row i of self and column j of other
                row.append(Matrix.dot(self.grid[i], column))
            new_grid.append(row)
        return Matrix(new_grid)

    @staticmethod
    def dot(lhs: list, rhs: list) -> float:
        """ Dot product of two list """
        if len(lhs) != len(rhs):
            raise ValueError

        # Simple Array dot product
        res = 0.0
        for i, left in enumerate(lhs):
            res += left * rhs[i]
        return res

    def __mul__(self, other):
        """ Multiply by others """

        # Call in the appropriate function for each types, give it's valid
        if isinstance(other, int):
            return self.multiply(other)
        if isinstance(other, Matrix):
            return self.times(other)
        raise TypeError

    def __reversed__(self):
        """ Inverted self """
        return self.inversed()

    def __pow__(self, power: int):
        """ Get power of matrix """
        if not self.is_square():
            raise ValueError("Cannot do operation with the given sizes for the matrices")

        # Multiply it self for each power - 1
        new_value = Matrix(self.grid)
        for _ in range(1, power):
            new_value = (new_value * self)
        return new_value

    def inversed(self):
        """ Inversed of self """

        # Validate size
        if not self.is_square():
            raise ValueError("Cannot do operation with the given sizes for the matrices")
        ide = Matrix.identity(self.size[0])

        # Try to create an echelon steps, and 
        new_grid = self.grid[:]
        for i, current in enumerate(new_grid):
            for j in range(i + 1, len(new_grid)):
                coef = new_grid[j][i] / current[i]

                # Apply the row operation to both the grid and the identity
                new_grid[j] = minus(new_grid[j], times(coef, current))
                ide[j] = minus(ide[j], times(coef, ide[i]))

        # Now try to eliminate all beside the pivots
        for i in range(len(new_grid)):
            rev = len(new_grid) - 1 - i
            for j in range(0, rev):
                coef = new_grid[j][rev] / new_grid[rev][rev]

                # Apply the row operation to both the grid and the identity
                new_grid[j] = minus(new_grid[j], times(coef, new_grid[rev]))
                ide[j] = minus(ide[j], times(coef, ide[rev]))

        # Try to eliminate all negatives
        for k, current in enumerate(new_grid):
            if current[k] < 0:
                new_grid[k] = times(-1, current)
                ide[k] = times(-1, ide[k])
        
        # Return the transformed identity
        return Matrix(ide)


def times(coef: float, array: list) -> list:
    """ Multiply a list by an float """
    return [(item * coef) for item in array]


def minus(lhs: list, rhs: list) -> list:
    """ reduce a list by another """
    return [lhs[i] - rhs[i] for i in range(len(lhs))]


if __name__ == '__main__':
    main()
