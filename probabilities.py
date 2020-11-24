"""
probabilities.py
Math for Probability
"""


def main():
    """ Main function """
    number = Fraction(10/4)
    print(number)


def common_factor(a: int, b: int) -> int:
    """ Get common factor of two ints"""
    if abs(a) > abs(b):
        res = abs(b)
    else:
        res = abs(a)
    while a % res != 0 or b % res != 0:
        res -= 1
    return res


class Fraction:
    """ Fraction object """

    def __init__(self, value, denominator: int = 1):
        """ Create self """
        if type(value) == float:
            num = round(100 * value - 10 * value)
            denom = 90
            fac = common_factor(num, denom)
            self.num = num // fac
            self.denom = denom // fac
        elif type(value) == int:
            fac = common_factor(value, denominator)
            self.num = value // fac
            self.denom = denominator // fac
        else:
            raise TypeError("Given Parameter cannot be converted into fraction")

    def __add__(self, other):
        """ Addition of fraction """
        if type(other) == int:
            return self.add_with_int(other)
        if type(other) == float:
            return self.add_with_float(other)
        if type(other) == Fraction:
            return self.add_with_fraction(other)
        raise TypeError("Cannot operate with that type")

    def add_with_fraction(self, other):
        """ Addition with fraction """
        if type(other) != Fraction:
            raise TypeError("Cannot operate with a non fraction")
        comfac = common_factor(self.denom, other.denom)
        new_denom = comfac * (self.denom / comfac) * (other.denom / comfac)
        copy = Fraction(1, 2)
        copy.denom = new_denom
        copy.num = self.num * (other.denom / comfac) + other.num * (self.denom / comfac)
        return Fraction(copy.num, copy.denom)

    def add_with_float(self, other: float):
        """ Addition with floats """
        new_other = Fraction(other)
        return self.add_with_fraction(new_other)

    def add_with_int(self, other: int):
        """ Addition with int """
        copy = Fraction(self.num, self.denom)
        copy.num += other * self.denom
        return Fraction(copy.num, copy.denom)

    def __sub__(self, other):
        """ Subtraction of fraction """
        if type(other) == int:
            return self.sub_with_int(other)
        if type(other) == float:
            return self.sub_with_float(other)
        if type(other) == Fraction:
            return self.sub_with_fraction(other)
        raise TypeError("Cannot operate with that type")

    def sub_with_fraction(self, other):
        """ Subtraction with fraction """
        if type(other) != Fraction:
            raise TypeError("Cannot operate with a non fraction")
        comfac = common_factor(self.denom, other.denom)
        new_denom = comfac * (self.denom / comfac) * (other.denom / comfac)
        copy = Fraction(1, 2)
        copy.denom = new_denom
        copy.num = self.num * (other.denom / comfac) - other.num * (self.denom / comfac)
        return Fraction(copy.num, copy.denom)

    def sub_with_float(self, other: float):
        """ Subtraction with floats """
        new_other = Fraction(other)
        return self.sub_with_fraction(new_other)

    def sub_with_int(self, other: int):
        """ Subtraction with int """
        copy = Fraction(self.num, self.denom)
        copy.num -= other * self.denom
        return Fraction(copy.num, copy.denom)

    def __mul__(self, other):
        """ Multiply of fraction """
        copy = Fraction(self.num, self.denom)
        if type(other) == int:
            copy.num *= other
            return copy
        if type(other) == float:
            return self.__mul__(Fraction(other))
        if type(other) == Fraction:
            copy.num *= other.num
            copy.denom *= other.denom
            return Fraction(copy.num, copy.denom)
        raise TypeError("Cannot operate with a non fraction")

    def __truediv__(self, other):
        """ Normal division of fraction """
        if type(other) == int:
            return Fraction(self.num, self.denom * other)
        if type(other) == float:
            return self.__truediv__(Fraction(other))
        if type(other) == Fraction:
            return self.__mul__(Fraction(other.denom, other.num))
        return TypeError("Cannot operate with a non fraction")

    def __floordiv__(self, other) -> int:
        """ Floor division of fraction """
        answer = self.__truediv__(other)
        return answer.num // answer.denom

    def __mod__(self, other) -> int:
        """ Modulo of fraction """
        answer = self.__truediv__(other)
        return answer.num % answer.denom

    def __divmod__(self, other):
        """ Get the div and mod of fraction """
        return self.__floordiv__(other), self.__mod__(other)

    def __pow__(self, power, modulo=None):
        """ The power of fraction """
        return Fraction(self.num ** power, self.denom ** power)

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
