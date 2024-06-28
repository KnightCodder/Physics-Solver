import math

class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        if self.z == 0.0:
            return f"({self.x}, {self.y})"
        else:
            return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Can only add two vectors")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("Can only subtract two vectors")
    
    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot_product(self, other) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError("Can only compute dot product with another vector")

    def cross_product(self, other):
        if isinstance(other, Vector):
            return Vector(self.y * other.z - self.z * other.y,
                          self.z * other.x - self.x * other.z,
                          self.x * other.y - self.y * other.x)
        else:
            raise ValueError("Can only compute cross product with another vector")
