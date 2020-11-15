"""
augmented_matrix.py
authored by Vincent
"""


def main():
    """ Main function """
    system = [
        [1, 0, 0, 9],
        [1, 1, 1, 10],
        [1, 0, 1, 12]
    ]
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
        for i in range(len(new_value)):
            if i < len(new_value) - 1:
                for j in range(i + 1, len(new_value)):
                    coef = new_value[j][i] / new_value[i][i]
                    new_value[j] = minus(new_value[j], times(coef, new_value[i]))
        return new_value

    def echelon_with_steps(self):
        """ Row echelon form of self """
        new_value = [self.matrix[i] + [self.result[i]] for i in range(len(self.matrix))]
        print("Step begin here")
        for i in range(len(new_value)):
            if i < len(new_value) - 1:
                for j in range(i + 1, len(new_value)):
                    coef = new_value[j][i] / new_value[i][i]
                    new_value[j] = minus(new_value[j], times(coef, new_value[i]))
                for row in new_value:
                    print(row)
                print("vvvvvvv")
        return new_value


def echelon(aug_matrix: list) -> list:
    """ Return a row echelon form of block matrix """
    new_value = aug_matrix[:]
    for i in range(len(new_value)):
        if i < len(new_value) - 1:
            for j in range(i + 1, len(new_value)):
                coef = new_value[j][i] / new_value[i][i]
                new_value[j] = minus(new_value[j], times(coef, new_value[i]))
    return new_value


def echelon_with_steps(aug_matrix: list) -> list:
    """ Return a row echelon form of block matrix """
    new_value = aug_matrix[:]
    print("Steps begins here")
    for i in range(len(new_value)):
        if i < len(new_value) - 1:
            for j in range(i + 1, len(new_value)):
                coef = new_value[j][i] / new_value[i][i]
                new_value[j] = minus(new_value[j], times(coef, new_value[i]))
            for row in new_value:
                print(row)
            print("vvvvvvv")
    return new_value


def times(coef: int, array: list) -> list:
    return [(item * coef) for item in array]


def minus(lhs: list, rhs: list) -> list:
    return [lhs[i] - rhs[i] for i in range(len(lhs))]


if __name__ == '__main__':
    main()
