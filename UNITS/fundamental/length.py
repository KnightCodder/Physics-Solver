from MATH.vector import Vector

ALLOWED_UNITS = {'m': 1, 'cm': 0.01, 'km': 1000}

class Displacement:
    def __init__(self, value: Vector, unit: str):
        if unit not in ALLOWED_UNITS:
            raise ValueError(f"Unit {unit} is not allowed. Allowed units: {ALLOWED_UNITS.keys()}")
        
        self.value = value
        self.unit = unit

    def conversion(self, unit: str):
        if unit not in ALLOWED_UNITS:
            raise ValueError(f"Unit {unit} is not allowed. Allowed units: {ALLOWED_UNITS.keys()}")
        
        self.value.x *= ALLOWED_UNITS[self.unit] / ALLOWED_UNITS[unit]
        self.value.y *= ALLOWED_UNITS[self.unit] / ALLOWED_UNITS[unit]
        self.value.z *= ALLOWED_UNITS[self.unit] / ALLOWED_UNITS[unit]
        self.unit = unit

    def __repr__(self):
        return f"{self.value} {self.unit}"
    
    def __add__(self, other):
        if isinstance(other, Displacement):
            if ALLOWED_UNITS[self.unit] > ALLOWED_UNITS[other.unit]:
                other.conversion(self.unit)
            else:
                self.conversion(other.unit)
            return Displacement(self.value + other.value, self.unit)
        else:
            raise ValueError("Cannot add different quantities")

    def __sub__(self, other):
        if isinstance(other, Displacement):
            if ALLOWED_UNITS[self.unit] > ALLOWED_UNITS[other.unit]:
                other.conversion(self.unit)
            else:
                self.conversion(other.unit)
            return Displacement(self.value - other.value, self.unit)
        else:
            raise ValueError("Cannot subtract different quantities")

