"""
probabilities.py
Math for Probability
authored by Vincent
version 1.0.2
last modified Nov 28, 2020 at 3:59 PM (UTC + 7)
Copyright © 2020 Vincent. All rights reserved.
"""


def main():
    """ Main function """
    number = Fraction(10/4)
    print(number)


def common_factor(num_a: int, num_b: int) -> int:
    """ Get common factor of two ints"""
    if abs(num_a) > abs(num_b):
        res = abs(num_b)
    else:
        res = abs(num_a)
    while num_a % res != 0 or num_b % res != 0:
        res -= 1
    return res


class Fraction:
    """ Fraction object """

    def __init__(self, value, denominator: int = 1):
        """ Create self """

        # for given first value is a float, no given denominator
        if isinstance(value, float) and denominator == 1:

            # Convert that float in a numerator and denominator using
            num = round(100 * value - 10 * value)
            # 100 n - 10 n = 90n that meant denominator is 90
            denom = 90

            # Make sure both is factored by their common factor
            fac = common_factor(num, denom)
            self.num = num // fac
            self.denom = denom // fac
        
        # For two int parameter
        elif isinstance(value, int):

            # Just get the common factor and simply both
            fac = common_factor(value, denominator)
            self.num = value // fac
            self.denom = denominator // fac
        else:
            raise TypeError("Given Parameter cannot be converted into fraction")

    def __add__(self, other):
        """ Addition of fraction """

        # Determine what type is given
        if isinstance(other, int):
            return self.add_with_int(other)
        if isinstance(other, float):
            return self.add_with_float(other)
        if isinstance(other, Fraction):
            return self.add_with_fraction(other)
        raise TypeError("Cannot operate with that type")

    def add_with_fraction(self, other):
        """ Addition with fraction """
        if not isinstance(other, Fraction):
            raise TypeError("Cannot operate with a non fraction")

        # get common factor of both denominator, create a new one using that
        comfac = common_factor(self.denom, other.denom)
        new_denom = comfac * (self.denom / comfac) * (other.denom / comfac)

        # Create a new result fraction object, then change the denominator
        copy = Fraction(1, 2)
        copy.denom = new_denom

        # Change the numerator to the it times what denom is multiplied by
        copy.num = self.num * (other.denom / comfac) + other.num * (self.denom / comfac)
        return Fraction(copy.num, copy.denom)

    def add_with_float(self, other: float):
        """ Addition with floats """
        new_other = Fraction(other)
        return self.add_with_fraction(new_other)

    def add_with_int(self, other: int):
        """ Addition with int """
        if not isinstance(other, int):
            raise TypeError("Cannot operate with a non integer")

        # Add the numerator by the given times the denominator
        copy = Fraction(self.num, self.denom)
        copy.num += other * self.denom
        return Fraction(copy.num, copy.denom)

    def __sub__(self, other):
        """ Subtraction of fraction """

        # Determine what type is given
        if isinstance(other, int):
            return self.sub_with_int(other)
        if isinstance(other, float):
            return self.sub_with_float(other)
        if isinstance(other, Fraction):
            return self.sub_with_fraction(other)
        raise TypeError("Cannot operate with that type")

    def sub_with_fraction(self, other):
        """ Subtraction with fraction """
        if not isinstance(other, Fraction):
            raise TypeError("Cannot operate with a non fraction")

        # get common factor of both denominator, create a new one using that
        comfac = common_factor(self.denom, other.denom)
        new_denom = comfac * (self.denom / comfac) * (other.denom / comfac)

        # Create a new result fraction object, then change the denominator
        copy = Fraction(1, 2)
        copy.denom = new_denom

        # Change the numerator to the it times what denom is multiplied by
        copy.num = self.num * (other.denom / comfac) - other.num * (self.denom / comfac)
        return Fraction(copy.num, copy.denom)

    def sub_with_float(self, other: float):
        """ Subtraction with floats """
        new_other = Fraction(other)
        return self.sub_with_fraction(new_other)

    def sub_with_int(self, other: int):
        """ Subtraction with int """
        if not isinstance(other, int):
            raise TypeError("Cannot operate with a non integer")

        # Subtract the numerator by the given times the denominator
        copy = Fraction(self.num, self.denom)
        copy.num -= other * self.denom
        return Fraction(copy.num, copy.denom)

    def __mul__(self, other):
        """ Multiply of fraction """
        copy = Fraction(self.num, self.denom)

        # If it's an int just multiply the numerator
        if isinstance(other, int):
            copy.num *= other
            return copy

        # If it's a float, convert to fraction, then re do multiplcation
        if isinstance(other, float):
            return self.__mul__(Fraction(other))

        # if it's a fraction, times the numerator and denominator
        if isinstance(other, Fraction):
            copy.num *= other.num
            copy.denom *= other.denom
            return Fraction(copy.num, copy.denom)
        raise TypeError("Cannot operate with a non fraction")

    def __truediv__(self, other):
        """ Normal division of fraction """

        # If it's an int just multiply the denominator
        if isinstance(other, int):
            return Fraction(self.num, self.denom * other)
        
        # If it's a float, convert to fraction, then re do division
        if isinstance(other, float):
            return self.__truediv__(Fraction(other))

        # if it's a fraction times the numerator and denominator, but inverted
        if isinstance(other, Fraction):
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


def permute(num: int, p_num: int) -> float:
    """ Get permutation of n to p """
    return factorial(num) / factorial(num - p_num)


def combine(num: int, p_num: int) -> float:
    """ Return combination of n to p """
    return factorial(num) / (factorial(num - p_num) * factorial(p_num))


if __name__ == '__main__':
    main()
