ALLOWED_UNITS = {'kg': 1, 'g': 0.001, 'lb': 0.453592}

class Mass:
    def __init__(self, value: float, unit: str):
        if value < 0:
            raise ValueError("Mass can never be negative")
        if unit not in ALLOWED_UNITS:
            raise ValueError(f"Unit {unit} is not allowed. Allowed units: {ALLOWED_UNITS.keys()}")
        
        self.value = value
        self.unit = unit

    def conversion(self, unit: str):
        if unit not in ALLOWED_UNITS:
            raise ValueError(f"Unit {unit} is not allowed. Allowed units: {ALLOWED_UNITS.keys()}")
        
        self.value *= ALLOWED_UNITS[self.unit] / ALLOWED_UNITS[unit]
        self.unit = unit

    def __repr__(self):
        return f"{self.value} {self.unit}"
    
    def __add__(self, other):
        if isinstance(other, Mass):
            if ALLOWED_UNITS[self.unit] > ALLOWED_UNITS[other.unit]:
                other.conversion(self.unit)
            else:
                self.conversion(other.unit)
            return Mass(self.value + other.value, self.unit)
        else:
            raise ValueError("Cannot add different quantities")

    def __sub__(self, other):
        if isinstance(other, Mass):
            if ALLOWED_UNITS[self.unit] > ALLOWED_UNITS[other.unit]:
                other.conversion(self.unit)
            else:
                self.conversion(other.unit)
            return Mass(self.value - other.value, self.unit)
        else:
            raise ValueError("Cannot subtract different quantities")
