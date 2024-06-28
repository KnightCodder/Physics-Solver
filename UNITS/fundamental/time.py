ALLOWED_UNITS = {'s': 1, 'min': 60, 'hrs': 3600}

class Time:
    def __init__(self, value: float, unit: str):
        if value < 0:
            raise ValueError("time can never be negative")
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
        if isinstance(other, Time):
            if ALLOWED_UNITS[self.unit] > ALLOWED_UNITS[other.unit]:
                other.conversion(self.unit)
            else:
                self.conversion(other.unit)
            return Time(self.value + other.value, self.unit)
        else:
            raise ValueError("Cannot add different quantities")

    def __sub__(self, other):
        if isinstance(other, Time):
            if ALLOWED_UNITS[self.unit] > ALLOWED_UNITS[other.unit]:
                other.conversion(self.unit)
            else:
                self.conversion(other.unit)
            return Time(self.value - other.value, self.unit)
        else:
            raise ValueError("Cannot subtract different quantities")
