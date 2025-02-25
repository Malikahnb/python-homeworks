import math


class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can only add Vector to Vector")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("You can only subtract Vector from Vector")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar multiplication requires number")
        return Vector(*(a * scalar for a in self.components))

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Dot product requires another Vector")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self * (1 / mag)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.components == other.components
