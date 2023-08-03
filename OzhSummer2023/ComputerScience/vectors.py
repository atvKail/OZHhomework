import numpy as np
import math


class Vector2D:
    x, y = 0, 0
    magnitude = pow((x ** 2 + y ** 2), 0.5)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = pow((x ** 2 + y ** 2), 0.5)

    def angle(self, r, _roundUp=12):
        return round(math.acos(self.scalarProduct(r) / (self.magnitude * r.magnitude)) / math.pi * 180, _roundUp)

    def scalarProduct(self, Vx):
        return Vx.x * Vx.x + Vx.y * Vx.y

    def convertNumpyArray(self):
        return np.array(self.x, self.y)

    def normalize(self):
        self.x /= self.magnitude
        self.y /= self.magnitude
        self.magnitude = pow((self.x ** 2 + self.y ** 2), 0.5)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.magnitude = pow((self.x ** 2 + self.y ** 2), 0.5)
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.magnitude = pow((self.x ** 2 + self.y ** 2), 0.5)
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, other):
        return Vector3D(0, 0, self.x * other.y - self.y * other.x)


class Vector3D:
    x, y, z = 0, 0, 0
    magnitude = 0

    def __int__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.magnitude = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = pow((x ** 2 + y ** 2 + z ** 2), 0.5)

    def angle(self, r, _roundUp=12):
        return round(math.acos(self.scalarProduct(r) / (self.magnitude * r.magnitude)) / math.pi * 180, _roundUp)

    def scalarProduct(self, Vx):
        return self.x * Vx.x + self.y * Vx.y + self.z * Vx.z

    def convertNumpyArray(self):
        return np.array(self.x, self.y)

    def normalize(self):
        self.x /= self.magnitude
        self.y /= self.magnitude
        self.z /= self.magnitude
        self.magnitude = pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.magnitude = pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
        return self

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        self.magnitude = pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y, self.z)

    def __bool__(self):
        return self.x != 0 or self.y != 0 or self.z

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)
