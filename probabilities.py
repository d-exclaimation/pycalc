"""
probabilities.py
Math for Probability
"""


def main():
    """ Main function """
    number = Fraction(10/4)
    print(number)


def common_factor(a: int, b: int) -> int:
    """ Get common factor of two ints """
    if abs(a) > abs(b):
        res = abs(b)
    else:
        res = abs(a)
    while a % res != 0 or b % res != 0:
        res -= 1
    return res


class Fraction:
    """ Fraction object """

    def __init__(self, value: float):
        """ Create self """
        num = round(100 * value - 10 * value)
        denom = 90
        fac = common_factor(num, denom)
        self.num = num // fac
        self.denom = denom // fac

    def __add__(self, other: int):
        """ Addition of fraction """
        copy = Fraction(self.num / self.denom)
        copy.num += other * self.denom
        return copy

    def __str__(self) -> str:
        """ Get string represent of self """
        return str(self.num) + "/" + str(self.denom)


def factorial(value):
    """ Return factorial of value """
    if value <= 1:
        return 1
    return value * factorial(value - 1)


def permute(n: int, p: int) -> float:
    """ Get permutation of n to p """
    return factorial(n) / factorial(n - p)


def combine(n: int, p: int) -> float:
    """ Return combination of n to p """
    return factorial(n) / (factorial(n - p) * factorial(p))


if __name__ == '__main__':
    main()
