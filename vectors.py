"""
vectors.py
Math for Vectors
authored by Vincent
version 1.0.2
last modified Nov 28, 2020 at 3:59 PM (UTC + 7)
Copyright © 2020 Vincent. All rights reserved.
"""
import math


def main():
    """ Main function"""
    print(help(Vector2))


def parallelogram(lhs, rhs):
    """ Find area of parallelogram """
    if isinstance(lhs, type(rhs)) and type(lhs) not in [Vector2, Vector3, VectorAny]:
        raise TypeError("Cannot do dot product with a non Vector")
    return (lhs * rhs).magnitude()


def triangle(lhs, rhs):
    """ Get area of triangle """
    return parallelogram(lhs, rhs) / 2


class Vector2:
    """ Vector of x and y """

    def __init__(self, x, y):
        """ Create self """
        self.array = [x, y]

    def get_x(self):
        """ X Axis value """
        return self.array[0]

    def get_y(self):
        """ Y axis value """
        return self.array[1]

    def __add__(self, other):
        """ Add self """
        new = Vector2(self.get_x(), self.get_y())
        if not isinstance(other, Vector2):
            raise TypeError("Cannot do add product with a non Vector2")
        for i in range(len(new.array)):
            new.array[i] = new.array[i] + other.array[i]
        return new

    def __sub__(self, other):
        """ Subtract self """
        new = Vector2(self.get_x(), self.get_y())
        if not isinstance(other, Vector2):
            raise TypeError("Cannot do min product with a non Vector2")
        for i in range(len(new.array)):
            new.array[i] = new.array[i] - other.array[i]
        return new

    def dot(self, other):
        """ Dot product """
        if not isinstance(other, Vector2):
            raise TypeError("Cannot do dot product with a non Vector2")
        res = 0.0
        for i in range(len(self.array)):
            res += self.array[i] * other.array[i]
        return res

    def __str__(self):
        """ String self """
        return "Vector2 ({0}, {1})".format(self.array[0], self.array[1])

    def magnitude(self):
        """ Magnitude """
        res = 0.0
        for i in self.array:
            res += (i ** 2)
        return math.sqrt(res)

    def is_orthogonal(self, other) -> bool:
        """ Check if two vector is orthogonal to each other """
        return self.dot(other) == 0

    @staticmethod
    def zero():
        """ Zero of Vector2 """
        return Vector2(0, 0)


class Vector3:
    """ Vector of 3 axis """

    def __init__(self, x, y, z):
        """ Constructor """
        self.axises = [x, y, z]

    @staticmethod
    def zero():
        """ Zero Vector3 """
        return Vector3(0, 0, 0)

    def get_x(self):
        """ X Axis value """
        return self.axises[0]

    def get_y(self):
        """ Y Axis value """
        return self.axises[1]

    def get_z(self):
        """ Z Axis value """
        return self.axises[2]

    def __str__(self):
        """ String self """
        return "Vector3 ({0}, {1}, {2})".format(self.get_x(), self.get_y(), self.get_z())

    def __add__(self, other):
        """ Add two vector3 """
        new = Vector3(self.get_x(), self.get_y(), self.get_z())
        if not isinstance(other, Vector3):
            raise TypeError("Cannot do add product with a non Vector3")
            
        # Add all element of the vectors of self and the other
        for i in range(len(new.axises)):
            new.axises[i] = new.axises[i] + other.axises[i]
        return new

    def __sub__(self, other):
        """ Subtract two vector3 """
        new = Vector3(self.get_x(), self.get_y(), self.get_z())
        if not isinstance(other, Vector3):
            raise TypeError("Cannot do min product with a non Vector3")
            
        # Subtract all element of the vectors of self and the other
        for i in range(len(new.axises)):
            new.axises[i] = new.axises[i] - other.axises[i]
        return new

    def __mul__(self, other):
        """ Cross product """
        if not isinstance(other, Vector3):
            raise TypeError("Cannot do cross product with a non Vector3")

        # Get a new Vector 3 as result
        new_value = Vector3.zero()

        # Loop through for each axises
        for i in range(len(self.axises)):

            # Get all the axises beside the currently checked on
            lhs = [self.axises[j] for j in range(len(self.axises)) if j != i]
            rhs = [other.axises[k] for k in range(len(other.axises)) if k != i]

            # Find the determinant and put in the result for the current index
            deter = (lhs[0] * rhs[1]) - (lhs[1] * rhs[0])
            new_value.axises[i] = deter
        return new_value

    def dot(self, other):
        """ Dot product of vector3 """
        if not isinstance(other, Vector3):
            raise TypeError("Cannot do dot product with a non Vector3")

        # Add all the multi of each axises from both
        res = 0.0
        for i in range(len(self.axises)):
            res += self.axises[i] * other.axises[i]
        return res

    def magnitude(self):
        """ Magnitude """
        res = 0.0
        for num in self.axises:
            res += num ** 2
        return res

    def is_orthogonal(self, other) -> bool:
        """ Check if two vector is orthogonal to each other """
        return self.dot(other) == 0


class VectorAny:
    """ Vector of size any """

    def __init__(self, *axises):
        """ Construct a Vector """
        res = []
        for axis in axises:
            res.append(axis)
        self.axises = res

    def __str__(self):
        """ String self """
        res = "("
        for axis in self.axises:
            res += " " + str(axis) + ","
        return res + ")"

    def __add__(self, other):
        """ Add two VectorAny """
        new = VectorAny(1)
        new.axises = self.axises
        if not isinstance(other, VectorAny) or len(other.axises) != len(self.axises):
            raise TypeError("Cannot add to a non VectorAny or VectorAny with different size")

        # Add all axises
        for i in range(len(new.axises)):
            new.axises[i] = new.axises[i] + other.axises[i]
        return new

    def __sub__(self, other):
        """ Substract two VectorAny """
        new = VectorAny(1)
        new.axises = self.axises
        if not isinstance(other, VectorAny) or len(other.axises) != len(self.axises):
            raise TypeError("Cannot add to a non VectorAny or VectorAny with different size")

        # Subtract all axises
        for i in range(len(new.axises)):
            new.axises[i] = new.axises[i] - other.axises[i]
        return new

    def dot(self, other):
        """ Dot product of VectorAny """
        if not isinstance(other, VectorAny) or len(other.axises) != len(self.axises):
            raise TypeError("Cannot add to a non VectorAny or VectorAny with different size")

        # Add all multiplication of each axises from both
        res = 0.0
        for i in range(len(self.axises)):
            res += self.axises[i] * other.axises[i]
        return res

    def magnitude(self):
        """ Magnitude """
        res = 0.0
        for num in self.axises:
            res += num ** 2
        return res

    def is_orthogonal(self, other) -> bool:
        """ Check if two vector is orthogonal to each other """
        return self.dot(other) == 0


if __name__ == '__main__':
    main()
