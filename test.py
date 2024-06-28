from UNITS.fundamental.length import Displacement
from MATH.vector import Vector

a = Displacement(Vector(1,2,3), 'm')
b = Displacement(Vector(4,1,-6), 'cm')

print(a+b)
