"""
augmented_matrix.py
authored by Vincent
authored by Vincent
version 1.0.2
last modified Nov 28, 2020 at 3:59 PM (UTC + 7)
Copyright © 2020 Vincent. All rights reserved.
"""


def main():
    """ Main function """
    system = [
        [1, 0, 0, 9],
        [1, 1, 1, 10],
        [1, 0, 1, 12]
    ]
    aug_system = AugMatrix([row[:-1] for row in system], [row[-1] for row in system])
    aug_system.echelon_with_steps()
    echelon_with_steps(system)



class AugMatrix:
    """ Augmented Matrix """

    def __init__(self, core, res):
        """ Constructor """
        self.matrix = core
        self.result = res

    def echelon(self):
        """ Row echelon form of self """
        new_value = [self.matrix[i] + [self.result[i]] for i in range(len(self.matrix))]

        # Loop through each row
        for i, current in enumerate(new_value):

            # Check if it's a potential pivot
            if i < len(new_value) - 1:

                # Elimate all in the same column beside the pivot
                for j in range(i + 1, len(new_value)):
                    coef = new_value[j][i] / current[i]
                    new_value[j] = minus(new_value[j], times(coef, current))
        return new_value

    def echelon_with_steps(self):
        """ Row echelon form of self """
        new_value = [self.matrix[i] + [self.result[i]] for i in range(len(self.matrix))]

        # Loop through each row
        print("Step begin here")
        for i, current in enumerate(new_value):

            # Check if it's a potential pivot
            if i < len(new_value) - 1:

                # Elimate all in the same column beside the pivot
                for j in range(i + 1, len(new_value)):
                    coef = new_value[j][i] / current[i]
                    new_value[j] = minus(new_value[j], times(coef, current))

                # printing the grid in 2D
                for row in new_value:
                    print(row)
                print("vvvvvvv")
        return new_value


def echelon(aug_matrix: list) -> list:
    """ Return a row echelon form of block matrix """
    new_value = aug_matrix[:]

    # Loop through each row
    for i, current in enumerate(new_value):

        # Check if it's a potential pivot
        if i < len(new_value) - 1:

            # Elimate all in the same column beside the pivot
            for j in range(i + 1, len(new_value)):
                coef = new_value[j][i] / current[i]
                new_value[j] = minus(new_value[j], times(coef, current))
    return new_value


def echelon_with_steps(aug_matrix: list) -> list:
    """ Return a row echelon form of block matrix """
    new_value = aug_matrix[:]

    # Loop through each row
    print("Steps begins here")
    for i, current in enumerate(new_value):

        # Check if it's a potential pivot
        if i < len(new_value) - 1:

            # Elimate all in the same column beside the pivot
            for j in range(i + 1, len(new_value)):
                coef = new_value[j][i] / current[i]
                new_value[j] = minus(new_value[j], times(coef, current))

            # printing the grid in 2D
            for row in new_value:
                print(row)
            print("vvvvvvv")
    return new_value


def times(coef: int, array: list) -> list:
    """ Time an array with an int """
    return [(item * coef) for item in array]


def minus(lhs: list, rhs: list) -> list:
    """ Reduce an array by another one"""
    return [lhs[i] - rhs[i] for i in range(len(lhs))]


if __name__ == '__main__':
    main()
